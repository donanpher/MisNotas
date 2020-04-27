#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Mis Notas.py, v.1.2
#  una sencilla aplicación para guardar notas.
#  
#  Copyright April, 2020 fer <donanpher@gmail.com>
#  (durante la cuarentena del Coronavirus Covid-19)
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sqlite3, sys, os
from PyQt5.QtWidgets import QDialog, QApplication,QTableWidgetItem,QInputDialog
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox
from sqlite3 import Error
from datetime import date
from datetime import datetime
from ui_misnotas import *
BaseDeDatos = "misnotas.db"

class MyForm(QDialog):
    botonBuscar = True # es para conmutar entre Buscar/Actualizar

    def __init__(self):
        super().__init__()
        #super(MyForm, self).__init__(parent,flags=QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowCloseButtonHint)
        if not os.path.isfile(BaseDeDatos): # si no existe la bb.dd., la creamos
            self.CrearDB()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./images/kwrite_writing_book_pencil_note_6093.ico'))
        self.setFixedSize(self.size()) # fijamos el tamaño de la ventana para que no se pueda cambiar
        self.MostrarTabla("SELECT * FROM notas ORDER BY Fecha DESC, ID DESC;",())
        self.ui.labelID.hide() # ocultamos la label del ID que usamos para distinguir entre alta/modificación de una nota
        self.ui.labelFecha.hide() # ocultamos label fecha, pues solo se habilita en las modificaciones. En las altas lo ponemos automático
        self.ui.lineEditFecha.hide() # lo mismo para el lineedit de la fecha
        self.ui.labelResponse.setStyleSheet('color: red')
        self.ui.pushButtonGuardar.clicked.connect(self.Guardar)
        self.ui.pushButtonModificar.clicked.connect(self.Modificar)
        self.ui.pushButtonEliminar.clicked.connect(self.Eliminar)
        self.ui.pushButtonBuscar.clicked.connect(self.Buscar)
        self.ui.pushButtonSalir.clicked.connect(self.close)
        self.ui.labelImagen.mouseReleaseEvent = self.MuestraCreditos # mousePressEvent() , mouseReleaseEvent() , mouseDoubleClickEvent()
        self.botonBuscar = True
        self.show()

    def MuestraCreditos(self, jj):
        QMessageBox.about(self, "Información", "Fer ha hecho esta simple aplicación \ndonanpher@gmail.com \nAbril 2020 \n(durante la cuarentena del Coronavirus COVID-19)")

    def ActualizarTableWidget(self, miQuery, tuplaQuery):
        self.ui.labelResponse.setText("") # borramos cualquier mensaje de alerta anterior
        self.ui.tableWidgetNotas.clear()
        self.MostrarTabla(miQuery, tuplaQuery)

    def MostrarTabla(self, miQuery, tuplaQuery):
        self.ui.labelResponse.setText("") # borramos cualquier mensaje de alerta anterior
        try:
            conn = sqlite3.connect(BaseDeDatos)
            cur = conn.cursor()
            if len(tuplaQuery) == 0:
                cur.execute(miQuery)
            else:
                cur.execute(miQuery, tuplaQuery)
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
            # Geometría de la tabla
            self.ui.tableWidgetNotas.setColumnWidth(0,0) # ancho columna ID
            self.ui.tableWidgetNotas.setColumnWidth(1,90) # ancho columna Fecha
            self.ui.tableWidgetNotas.setColumnWidth(2,70) # ancho columna Tag
            self.ui.tableWidgetNotas.setColumnWidth(3,280) # ancho columna Nota
            self.ui.tableWidgetNotas.resizeRowsToContents() # ajuste alto de fila a su contenido
            self.ui.labelTotalReg.setText("Total Notas: " + str(totalReg))
            self.ui.tableWidgetNotas.setHorizontalHeaderLabels(("ID","Fecha","Tag","Nota"))
            #self.ui.tableWidgetNotas.horizontalHeaderItem().setTextAlignment(AlignHCenter)

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
        elTag = self.ui.lineEditTag.text()
        conn = sqlite3.connect(BaseDeDatos)
        cur = conn.cursor()
        elID = int(self.ui.labelID.text())
        tuplaQuery = ()
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
            #laQuery = "INSERT INTO notas (Fecha, Tag, Nota) VALUES ('" + str(laFecha) + "', '" + str(elTag) + "', '" + laNota + "')"
            laQuery = "INSERT INTO notas (Fecha, Tag, Nota) VALUES (? , ?, ?)"
            tuplaQuery = (str(laFecha), str(elTag), laNota,)
        else:
            laFecha = self.ui.lineEditFecha.text()
            #laQuery = "UPDATE notas SET Fecha = '" + str(laFecha) + "', Tag = '" + str(elTag) + "', Nota = '" + laNota + "' WHERE ID = " + str(elID)
            laQuery = "UPDATE notas SET Fecha = ?, Tag = ?, Nota = ? WHERE ID = ?"
            tuplaQuery = (str(laFecha), str(elTag), laNota, str(elID),)
        #cur.execute(laQuery)
        cur.execute(laQuery, tuplaQuery)
        conn.commit()
        conn.close()
        self.ui.labelID.setText("0") # volvemos a poner a 0 este label
        self.ui.labelFecha.hide() # ocultamos label fecha, pues solo se habilita en las modificaciones. En las altas lo ponemos automático
        self.ui.lineEditFecha.setText("")
        self.ui.lineEditTag.setText("")
        self.ui.textEditNota.setPlainText("") # borramos el textEdit
        self.ui.lineEditFecha.hide() # lo mismo para el lineedit de la fecha

        # actualizamos el TableWidget
        self.ActualizarTableWidget("SELECT * FROM notas ORDER BY Fecha DESC, ID DESC;", ())

    def Modificar(self):
        self.ui.labelResponse.setText("") # borramos cualquier mensaje de alerta anterior
        laFila = self.ui.tableWidgetNotas.currentRow()
        if laFila == -1:
            self.ui.labelResponse.setText("Selecciona la fila para modificar")
        else:
            elID = self.ui.tableWidgetNotas.item(laFila, 0).text()
            laFecha = self.ui.tableWidgetNotas.item(laFila, 1).text()
            elTag = self.ui.tableWidgetNotas.item(laFila, 2).text()
            elContenido = self.ui.tableWidgetNotas.item(laFila, 3).text()
            self.ui.labelID.setText(elID)
            self.ui.lineEditFecha.setText(laFecha)
            self.ui.lineEditTag.setText(elTag)
            self.ui.textEditNota.setPlainText(elContenido)
            self.ui.labelFecha.show() # mostramos label fecha para habilitar la modificación
            self.ui.lineEditFecha.show() # lo mismo para el lineedit de la fecha


    def Eliminar(self):
        laFila = self.ui.tableWidgetNotas.currentRow()
        if laFila == -1:
            self.ui.labelResponse.setText("Selecciona la fila para eliminar")
        else:
            elID = self.ui.tableWidgetNotas.item(laFila, 0).text()
            laNota = self.ui.tableWidgetNotas.item(laFila, 3).text()
            buttonReply = QMessageBox.question(self, 'Eliminar Nota', "¿Quieres eliminar esta nota?:\n" + laNota, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                conn = sqlite3.connect(BaseDeDatos)
                cur = conn.cursor()
                #laQuery = "DELETE FROM notas WHERE ID = " + str(elID)
                laQuery = "DELETE FROM notas WHERE ID = ?"
                cur.execute(laQuery, (str(elID),))
                conn.commit()
                conn.close()
                # actualizamos el TableWidget
                self.ActualizarTableWidget("SELECT * FROM notas ORDER BY Fecha DESC, ID DESC;",())

    def Buscar(self):
        if not self.botonBuscar: # si ya se ha hecho una búsqueda, cambiamos el label para que sea Actualizar
            self.ActualizarTableWidget("SELECT * FROM notas ORDER BY Fecha DESC, ID DESC;",())
            self.botonBuscar = True
            self.ui.pushButtonBuscar.setText("&Buscar")
        else:
            campos = ("Fecha", "Tag", "Nota")
            elCampo, ok = QInputDialog.getItem(self, "Buscar 1/2", "Seleccionar campo:", campos, 0, False)
            if ok and elCampo:
                queBuscar, ok = QInputDialog.getText(self, "Buscar 2/2", "Qué buscar:")
                if ok and queBuscar:
                    #self.ActualizarTableWidget("SELECT * FROM notas WHERE " + elCampo + " LIKE '%" + queBuscar + "%' ORDER BY Fecha DESC, ID DESC;",())
                    self.ActualizarTableWidget("SELECT * FROM notas WHERE " + elCampo + " LIKE ? ORDER BY Fecha DESC, ID DESC;",("%" + queBuscar + "%",))
                    self.botonBuscar = False
                    self.ui.pushButtonBuscar.setText("&Actualizar")
            else: # si no se quiere buscar nada, mostramos todo
                self.ActualizarTableWidget("SELECT * FROM notas ORDER BY Fecha DESC, ID DESC;",())

    def CrearDB(self):
        try:
            conn = sqlite3.connect(BaseDeDatos)
            cur = conn.cursor()
            laQuery = "CREATE TABLE notas (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Fecha TEXT, Tag TEXT, Nota TEXT )"
            cur.execute(laQuery)
            conn.commit()
            laQuery = "INSERT INTO notas (Fecha, Tag, Nota) VALUES ('2020-01-01', 'prueba', 'Esta es la primera nota')"
            cur.execute(laQuery)
            conn.commit()
            conn.close()
        except ValueError as e:
            print(str(e))



if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
