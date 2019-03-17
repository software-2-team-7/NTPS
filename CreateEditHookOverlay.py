from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateEditHook(object):
    def setupUi(self, CreateEditHook):
        CreateEditHook.setObjectName("CreateEditHook")
        CreateEditHook.resize(545, 186)
        CreateEditHook.setMinimumSize(QtCore.QSize(545, 186))
        CreateEditHook.setMaximumSize(QtCore.QSize(545, 186))
        #CreateEditHook.setStyleSheet("background_color: rgb(255, 255, 255)\n")
        self.verticalLayout = QtWidgets.QVBoxLayout(CreateEditHook)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Frame_CreateEditHook = QtWidgets.QFrame(CreateEditHook)
        self.Frame_CreateEditHook.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_CreateEditHook.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_CreateEditHook.setObjectName("Frame_CreateEditHook")
        self.gridLayout = QtWidgets.QGridLayout(self.Frame_CreateEditHook)
        self.gridLayout.setObjectName("gridLayout")
        self.Label_Description = QtWidgets.QLabel(self.Frame_CreateEditHook)
        self.Label_Description.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_Description.setObjectName("Label_Description")
        self.gridLayout.addWidget(self.Label_Description, 2, 0, 1, 1)
        self.TextBox_HookName = QtWidgets.QLineEdit(self.Frame_CreateEditHook)
        self.TextBox_HookName.setAlignment(QtCore.Qt.AlignCenter)
        self.TextBox_HookName.setObjectName("TextBox_HookName")
        self.gridLayout.addWidget(self.TextBox_HookName, 1, 1, 1, 6)
        self.TextBox_Description = QtWidgets.QLineEdit(self.Frame_CreateEditHook)
        self.TextBox_Description.setAlignment(QtCore.Qt.AlignCenter)
        self.TextBox_Description.setObjectName("TextBox_Description")
        self.gridLayout.addWidget(self.TextBox_Description, 2, 1, 1, 6)
        self.TextBox_HookPath = QtWidgets.QLineEdit(self.Frame_CreateEditHook)
        self.TextBox_HookPath.setText("")
        self.TextBox_HookPath.setAlignment(QtCore.Qt.AlignCenter)
        self.TextBox_HookPath.setObjectName("TextBox_HookPath")
        self.gridLayout.addWidget(self.TextBox_HookPath, 3, 1, 1, 6)
        self.Button_Browse = QtWidgets.QPushButton(self.Frame_CreateEditHook)
        self.Button_Browse.setObjectName("Button_Browse")
        self.Button_Browse.clicked.connect(lambda: self.browseFile(self.TextBox_HookPath))
        self.gridLayout.addWidget(self.Button_Browse, 3, 7, 1, 1)
        self.Label_HookPath = QtWidgets.QLabel(self.Frame_CreateEditHook)
        self.Label_HookPath.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_HookPath.setObjectName("Label_HookPath")
        self.gridLayout.addWidget(self.Label_HookPath, 3, 0, 1, 1)
        self.Label_HookNam = QtWidgets.QLabel(self.Frame_CreateEditHook)
        self.Label_HookNam.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_HookNam.setObjectName("Label_HookNam")
        self.gridLayout.addWidget(self.Label_HookNam, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 6)

        self.buttonBox = QtWidgets.QDialogButtonBox(self.Frame_CreateEditHook)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Save | QtWidgets.QDialogButtonBox.Cancel)
        self.gridLayout.addWidget(self.buttonBox, 4, 6, 1, 2)

        self.verticalLayout.addWidget(self.Frame_CreateEditHook)

        self.save = False

        self.buttonBox.accepted.connect(lambda: self.setSave(CreateEditHook))
        self.buttonBox.rejected.connect(CreateEditHook.reject)

        self.retranslateUi(CreateEditHook)
        QtCore.QMetaObject.connectSlotsByName(CreateEditHook)

    def retranslateUi(self, CreateEditHook):
        _translate = QtCore.QCoreApplication.translate
        CreateEditHook.setWindowTitle(_translate("CreateEditHook", "Create/Edit Hook"))
        self.Label_Description.setText(_translate("CreateEditHook", "Description"))
        self.TextBox_Description.setPlaceholderText(_translate("CreateEditHook", "Description"))
        self.TextBox_HookPath.setPlaceholderText(_translate("CreateEditHook", "Hook Path"))
        self.Button_Browse.setText(_translate("CreateEditHook", "Browse"))
        self.TextBox_HookName.setPlaceholderText(_translate("CreateEditHook", "Hook Name"))
        self.Label_HookPath.setText(_translate("CreateEditHook", "Hook Path"))
        self.Label_HookNam.setText(_translate("CreateEditHook", "Hook Name"))

    def browseFile(self, textline):
        path, _ = QtWidgets.QFileDialog.getOpenFileName()
        textline.setText(path)

    def saveHook(self, dialogWindow, name):
        name.text()
        dialogWindow.close()

    def setSave(self, window):
        if(self.TextBox_HookName.text() != "" and self.TextBox_Description.text() != "" and self.TextBox_HookPath.text() != ""):
            self.save = True
        window.close()

    def getData(self, dialog):
        dialog.exec()
        if(self.save):
            hookname = self.TextBox_HookName.text()
            hookdes = self.TextBox_Description.text()
            hookpath = self.TextBox_HookPath.text()
            return hookname, hookdes, hookpath
        else:
            return "", "", ""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateEditHook = QtWidgets.QDialog()
    ui = Ui_CreateEditHook()
    ui.setupUi(CreateEditHook)
    CreateEditHook.show()
    sys.exit(app.exec_())
