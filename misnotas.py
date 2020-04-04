
import sqlite3, sys
from PyQt5.QtWidgets import QDialog, QApplication,QTableWidgetItem
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox
from sqlite3 import Error
from datetime import date
from datetime import datetime
from ui_misnotas import *
BaseDeDatos = "misnotas.db"

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        #super().__init__(parent,flags=Qt.WindowMinimizeButtonHint)
        #self.ui.setWindowFlags(dialog.windowFlags() | QtCore.Qt.WindowMinimizeButtonHint)
        #self.ui.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        #self.ui.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowMinimizeButtonHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.MostrarTabla("SELECT ID, Fecha, Nota FROM notas ORDER BY Fecha DESC, ID DESC;")
        self.ui.labelID.hide() # ocultamos la label del ID que usamos para distinguir entre alta/modificación de una nota
        self.ui.labelFecha.hide() # ocultamos label fecha, pues solo se habilita en las modificaciones. En las altas lo ponemos automático
        self.ui.lineEditFecha.hide() # lo mismo para el lineedit de la fecha
        self.ui.pushButtonGuardar.clicked.connect(self.Guardar)
        self.ui.pushButtonModificar.clicked.connect(self.Modificar)
        self.ui.pushButtonEliminar.clicked.connect(self.Eliminar)
        self.ui.pushButtonSalir.clicked.connect(self.close)
        self.show()

    def ActualizarTableWidget(self):
        self.ui.labelResponse.setText("") # borramos cualquier mensaje de alerta anterior
        self.ui.tableWidgetNotas.clear()
        self.MostrarTabla("SELECT ID, Fecha, Nota FROM notas ORDER BY Fecha DESC, ID DESC;")

    def MostrarTabla(self, miQuery):
        self.ui.labelResponse.setText("") # borramos cualquier mensaje de alerta anterior
        try:
            conn = sqlite3.connect(BaseDeDatos)
            cur = conn.cursor()
            cur.execute(miQuery)
            registros = cur.fetchall()
            totalReg = len(registros) # total de registros de la query
            self.ui.tableWidgetNotas.setRowCount(totalReg) # dimensionamos el widget en filas
            recNum = 0
            for tupla in registros:
                colNum = 0
                for columna in tupla:
                    unaColumna = QTableWidgetItem(str(columna))
                    self.ui.tableWidgetNotas.setItem(recNum, colNum, unaColumna)
                    colNum += 1
                recNum += 1
            self.ui.tableWidgetNotas.setColumnWidth(0,30) # ancho columna ID
            self.ui.tableWidgetNotas.setColumnWidth(1,90) # ancho columna Fecha
            self.ui.tableWidgetNotas.setColumnWidth(2,330) # ancho columna Nota
            self.ui.tableWidgetNotas.resizeRowsToContents() # ajuste alto de fila a su contenido

        except Error as e:
            #self.ui.tableWidgetNotas.clear()
            self.ui.labelResponse.setText(str(e))
        finally:
            conn.close()

    def Guardar(self):
            # Guardamos el reg. en la bb.dd.
            self.ui.labelResponse.setText("") # borramos cualquier mensaje de alerta anterior
            laNota = self.ui.textEditNota.toPlainText()
            if laNota == "":
                self.ui.labelResponse.setText("Nada que guardar!")
                return
            conn = sqlite3.connect(BaseDeDatos)
            cur = conn.cursor()
            elID = int(self.ui.labelID.text())
            if elID == 0: # si este label está a 0, es un alta, sino tendrá el ID del reg. que estamos modificando
                if self.ui.lineEditFecha.text() =="":
                    laFecha = str(date.today())
                else:
                    laFecha = self.ui.lineEditFecha.text()
                    try:
                        laFecha_obj = datetime.strptime(laFecha, "%Y-%m-%d")
                        laFecha = datetime.strftime(laFecha_obj, "%Y-%m-%d")
                    except ValueError as e:
                        self.ui.labelResponse.setText("Fecha incorrecta: respeta el formato aaaa-mm-dd")
                        self.ui.lineEditFecha.selectAll()
                        self.ui.lineEditFecha.setFocus()
                        conn.close()
                        return
                laQuery = "INSERT INTO notas (Fecha, Nota) VALUES ('" + str(laFecha) + "', '" + laNota + "')"

            else:
                laFecha = self.ui.lineEditFecha.text()
                laQuery = "UPDATE notas SET Fecha = '" + str(laFecha) + "', Nota = '" + laNota + "' WHERE ID = " + str(elID)

            cur.execute(laQuery)
            conn.commit()
            conn.close()
            self.ui.textEditNota.setPlainText("") # borramos el textEdit
            self.ui.labelID.setText("0") # volvemos a poner a 0 este label
            self.ui.lineEditFecha.setText("")
            self.ui.labelFecha.hide() # ocultamos label fecha, pues solo se habilita en las modificaciones. En las altas lo ponemos automático
            self.ui.lineEditFecha.hide() # lo mismo para el lineedit de la fecha

            # actualizamos el TableWidget
            self.ActualizarTableWidget()

    def Modificar(self):
        self.ui.labelResponse.setText("") # borramos cualquier mensaje de alerta anterior
        laFila = self.ui.tableWidgetNotas.currentRow()
        if laFila == -1:
            self.ui.labelResponse.setText("Selecciona la fila para modificar")
        else:
            elID = self.ui.tableWidgetNotas.item(laFila, 0).text()
            elContenido = self.ui.tableWidgetNotas.item(laFila, 2).text()
            laFecha = self.ui.tableWidgetNotas.item(laFila, 1).text()
            self.ui.labelID.setText(elID)
            self.ui.lineEditFecha.setText(laFecha)
            self.ui.textEditNota.setPlainText(elContenido)
            self.ui.labelFecha.show() # mostramos label fecha para habilitar la modificación
            self.ui.lineEditFecha.show() # lo mismo para el lineedit de la fecha


    def Eliminar(self):
        laFila = self.ui.tableWidgetNotas.currentRow()
        if laFila == -1:
            self.ui.labelResponse.setText("Selecciona la fila para eliminar")
        else:
            elID = self.ui.tableWidgetNotas.item(laFila, 0).text()
            buttonReply = QMessageBox.question(self, 'Eliminar Nota', "¿Quieres eliminar esta nota, \ncon ID=" + elID + "?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                conn = sqlite3.connect(BaseDeDatos)
                cur = conn.cursor()
                laQuery = "DELETE FROM notas WHERE ID = " + str(elID)
                cur.execute(laQuery)
                conn.commit()
                conn.close()
                # actualizamos el TableWidget
                self.ActualizarTableWidget()


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
