# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_misnotas.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(530, 463)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gallaecia Castelo")
        font.setPointSize(10)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/prefijo/images/kwrite_writing_book_pencil_note_6093.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.labelTitulo = QtWidgets.QLabel(Dialog)
        self.labelTitulo.setGeometry(QtCore.QRect(54, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Gallaecia Castelo")
        font.setPointSize(16)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName("labelTitulo")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(53, 35, 460, 10))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(68, 40, 241, 17))
        font = QtGui.QFont()
        font.setFamily("Gallaecia Castelo")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(475, 40, 40, 17))
        font = QtGui.QFont()
        font.setFamily("Gallaecia Castelo")
        font.setPointSize(7)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(140, 68, 110, 17))
        font = QtGui.QFont()
        font.setFamily("Gallaecia Castelo")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEditNota = QtWidgets.QTextEdit(Dialog)
        self.textEditNota.setGeometry(QtCore.QRect(140, 90, 371, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEditNota.setFont(font)
        self.textEditNota.setObjectName("textEditNota")
        self.pushButtonGuardar = QtWidgets.QPushButton(Dialog)
        self.pushButtonGuardar.setGeometry(QtCore.QRect(21, 142, 110, 29))
        font = QtGui.QFont()
        font.setFamily("Gallaecia Castelo")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonGuardar.setFont(font)
        self.pushButtonGuardar.setStyleSheet("image: url(:/otro/images/Note256_25041.ico);")
        self.pushButtonGuardar.setObjectName("pushButtonGuardar")
        self.tableWidgetNotas = QtWidgets.QTableWidget(Dialog)
        self.tableWidgetNotas.setEnabled(True)
        self.tableWidgetNotas.setGeometry(QtCore.QRect(20, 197, 491, 192))
        font = QtGui.QFont()
        font.setFamily("Gallaecia Castelo")
        font.setPointSize(10)
        self.tableWidgetNotas.setFont(font)
        self.tableWidgetNotas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetNotas.setAlternatingRowColors(True)
        self.tableWidgetNotas.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidgetNotas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetNotas.setRowCount(1)
        self.tableWidgetNotas.setColumnCount(4)
        self.tableWidgetNotas.setObjectName("tableWidgetNotas")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Gallaecia Castelo")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidgetNotas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Gallaecia Castelo")
        font.setPointSize(10)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidgetNotas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetNotas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Gallaecia Castelo")
        font.setPointSize(10)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidgetNotas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Gallaecia Castelo")
        font.setPointSize(10)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(9, 241, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.tableWidgetNotas.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Gallaecia Castelo")
        font.setPointSize(10)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(9, 241, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidgetNotas.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(9, 240, 248))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.tableWidgetNotas.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Gallaecia Castelo")
        font.setPointSize(10)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(9, 241, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.tableWidgetNotas.setItem(0, 3, item)
        self.pushButtonModificar = QtWidgets.QPushButton(Dialog)
        self.pushButtonModificar.setGeometry(QtCore.QRect(19, 422, 101, 29))
        font = QtGui.QFont()
        font.setFamily("Gallaecia Castelo")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonModificar.setFont(font)
        self.pushButtonModificar.setObjectName("pushButtonModificar")
        self.pushButtonEliminar = QtWidgets.QPushButton(Dialog)
        self.pushButtonEliminar.setGeometry(QtCore.QRect(148, 422, 101, 29))
        font = QtGui.QFont()
        font.setFamily("Gallaecia Castelo")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonEliminar.setFont(font)
        self.pushButtonEliminar.setObjectName("pushButtonEliminar")
        self.pushButtonSalir = QtWidgets.QPushButton(Dialog)
        self.pushButtonSalir.setGeometry(QtCore.QRect(410, 422, 101, 29))
        font = QtGui.QFont()
        font.setFamily("Gallaecia Castelo")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSalir.setFont(font)
        self.pushButtonSalir.setObjectName("pushButtonSalir")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(26, 176, 481, 20))
        self.labelResponse.setText("")
        self.labelResponse.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResponse.setObjectName("labelResponse")
        self.labelID = QtWidgets.QLabel(Dialog)
        self.labelID.setGeometry(QtCore.QRect(10, 60, 67, 17))
        self.labelID.setObjectName("labelID")
        self.lineEditFecha = QtWidgets.QLineEdit(Dialog)
        self.lineEditFecha.setGeometry(QtCore.QRect(412, 66, 100, 20))
        self.lineEditFecha.setMaxLength(10)
        self.lineEditFecha.setObjectName("lineEditFecha")
        self.labelFecha = QtWidgets.QLabel(Dialog)
        self.labelFecha.setGeometry(QtCore.QRect(277, 68, 140, 17))
        self.labelFecha.setObjectName("labelFecha")
        self.labelImagen = QtWidgets.QLabel(Dialog)
        self.labelImagen.setGeometry(QtCore.QRect(3, 2, 50, 40))
        self.labelImagen.setStyleSheet("border-image: url(:/prefijo/images/kwrite_writing_book_pencil_note_6093.ico);")
        self.labelImagen.setText("")
        self.labelImagen.setPixmap(QtGui.QPixmap("images/kwrite_writing_book_pencil_note_6093.ico"))
        self.labelImagen.setScaledContents(True)
        self.labelImagen.setObjectName("labelImagen")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(22, 91, 30, 17))
        font = QtGui.QFont()
        font.setFamily("Gallaecia Castelo")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEditTag = QtWidgets.QLineEdit(Dialog)
        self.lineEditTag.setGeometry(QtCore.QRect(50, 91, 80, 20))
        self.lineEditTag.setMaxLength(10)
        self.lineEditTag.setObjectName("lineEditTag")
        self.labelTotalReg = QtWidgets.QLabel(Dialog)
        self.labelTotalReg.setGeometry(QtCore.QRect(20, 390, 131, 17))
        self.labelTotalReg.setObjectName("labelTotalReg")
        self.pushButtonBuscar = QtWidgets.QPushButton(Dialog)
        self.pushButtonBuscar.setGeometry(QtCore.QRect(280, 422, 101, 29))
        font = QtGui.QFont()
        font.setFamily("Gallaecia Castelo")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonBuscar.setFont(font)
        self.pushButtonBuscar.setObjectName("pushButtonBuscar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEditFecha, self.lineEditTag)
        Dialog.setTabOrder(self.lineEditTag, self.textEditNota)
        Dialog.setTabOrder(self.textEditNota, self.pushButtonGuardar)
        Dialog.setTabOrder(self.pushButtonGuardar, self.tableWidgetNotas)
        Dialog.setTabOrder(self.tableWidgetNotas, self.pushButtonModificar)
        Dialog.setTabOrder(self.pushButtonModificar, self.pushButtonEliminar)
        Dialog.setTabOrder(self.pushButtonEliminar, self.pushButtonBuscar)
        Dialog.setTabOrder(self.pushButtonBuscar, self.pushButtonSalir)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Mis Notas"))
        self.labelTitulo.setText(_translate("Dialog", "Mis Notas"))
        self.label.setText(_translate("Dialog", "Pequeña aplicación para notas personales"))
        self.label_2.setText(_translate("Dialog", "v.1.1"))
        self.label_3.setText(_translate("Dialog", "Texto de la nota"))
        self.pushButtonGuardar.setText(_translate("Dialog", "&Guardar"))
        item = self.tableWidgetNotas.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.tableWidgetNotas.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Fecha"))
        item = self.tableWidgetNotas.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Tag"))
        item = self.tableWidgetNotas.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Nota"))
        __sortingEnabled = self.tableWidgetNotas.isSortingEnabled()
        self.tableWidgetNotas.setSortingEnabled(False)
        self.tableWidgetNotas.setSortingEnabled(__sortingEnabled)
        self.pushButtonModificar.setText(_translate("Dialog", "&Modificar"))
        self.pushButtonEliminar.setText(_translate("Dialog", "&Eliminar"))
        self.pushButtonSalir.setText(_translate("Dialog", "&Salir"))
        self.labelID.setText(_translate("Dialog", "0"))
        self.lineEditFecha.setToolTip(_translate("Dialog", "Fecha en formato ISO"))
        self.labelFecha.setText(_translate("Dialog", "Fecha (aaaa-mm-dd)"))
        self.label_4.setText(_translate("Dialog", "Tag"))
        self.lineEditTag.setToolTip(_translate("Dialog", "Introducir un Tag o Etiqueta"))
        self.labelTotalReg.setText(_translate("Dialog", "Total Notas:"))
        self.pushButtonBuscar.setText(_translate("Dialog", "&Buscar"))

import logoNotas_rc
