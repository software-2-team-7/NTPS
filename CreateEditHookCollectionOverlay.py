from PyQt5 import QtCore, QtGui, QtWidgets
from HookFunction.Hook import Hook
from HookFunction.HookCollection import HookCollection
from HookFunction.HookCollectionManager import HookCollectionManager


class Ui_Dialog(object):
    def setupUi(self, Dialog,manager):

        self.manager = manager

        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        #Dialog.setStyleSheet("background_color: rgb(255, 255, 255)\n")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.nameBox = QtWidgets.QLineEdit(self.frame_3)
        self.nameBox.setAlignment(QtCore.Qt.AlignCenter)
        self.nameBox.setObjectName("nameBox")
        self.gridLayout_2.addWidget(self.nameBox, 0, 1, 1, 1)
        
        self.collNameLabel = QtWidgets.QLabel(self.frame_3)
        self.collNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.collNameLabel.setObjectName("collNameLabel")
        self.gridLayout_2.addWidget(self.collNameLabel, 0, 0, 1, 1)
        
        self.descBox = QtWidgets.QLineEdit(self.frame_3)
        self.descBox.setAlignment(QtCore.Qt.AlignCenter)
        self.descBox.setObjectName("descBox")
        self.gridLayout_2.addWidget(self.descBox, 1, 1, 1, 1)
        
        self.seqBox = QtWidgets.QLineEdit(self.frame_3)
        self.seqBox.setAlignment(QtCore.Qt.AlignCenter)
        self.seqBox.setObjectName("seqBox")
        self.gridLayout_2.addWidget(self.seqBox, 3, 1, 1, 1)

        #Enable/Disable status button
        self.statusBox = QtWidgets.QComboBox(self.frame_3)
        self.statusBox.setTabletTracking(False)
        self.statusBox.setObjectName("statusBox")
        self.statusBox.addItem("")
        self.statusBox.addItem("")
        self.statusBox.addItem("")
        self.gridLayout_2.addWidget(self.statusBox, 2, 1, 1, 1)
        #End Enale/Disable status button

        #Labels
        self.descLabel = QtWidgets.QLabel(self.frame_3)
        self.descLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.descLabel.setObjectName("descLabel")
        self.gridLayout_2.addWidget(self.descLabel, 1, 0, 1, 1)
        self.statusLabel = QtWidgets.QLabel(self.frame_3)
        self.statusLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statusLabel.setObjectName("statusLabel")
        self.gridLayout_2.addWidget(self.statusLabel, 2, 0, 1, 1)
        self.sequenceLabel = QtWidgets.QLabel(self.frame_3)
        self.sequenceLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sequenceLabel.setObjectName("sequenceLabel")
        self.gridLayout_2.addWidget(self.sequenceLabel, 3, 0, 1, 1)
        #Labels End

        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 590, 257))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")

        #Hook labels
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 3, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 5, 1, 1)

        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 0, 2, 8, 1)

        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 0, 4, 8, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 6, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Save | QtWidgets.QDialogButtonBox.Cancel)
        self.horizontalLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Create/Edit Hook Collection"))
        self.nameBox.setPlaceholderText(_translate("Dialog", "Hook Collection Name"))
        self.descBox.setPlaceholderText(_translate("Dialog", "Hook Collection Description"))
        self.seqBox.setPlaceholderText(_translate("Dialog", "Enter Sequence No."))
        
        
        #Drop box
        self.statusBox.setCurrentText(_translate("Dialog", "Enabled/Disabled"))
        self.statusBox.setItemText(0, _translate("Dialog", "Enabled/Disabled"))
        self.statusBox.setItemText(1, _translate("Dialog", "Enabled"))
        self.statusBox.setItemText(2, _translate("Dialog", "Disabled"))
        #Drop box end
        
        self.collNameLabel.setText(_translate("Dialog", "Hook Collection Name"))
        self.descLabel.setText(_translate("Dialog", "Description"))
        self.statusLabel.setText(_translate("Dialog", "Status"))
        self.sequenceLabel.setText(_translate("Dialog", "Execution Sequence"))
        #End of collection information

        self.label.setText(_translate("Dialog", "Hook"))
        self.label_2.setText(_translate("Dialog", "Status"))
        self.label_3.setText(_translate("Dialog", "Hook Execution Sequence"))
    
    def updateHookBox(self):
        
        rowNum = 1

        for h in self.manager.getHooks(): #for each hook, generate a row with all contents
            
            #adds checkbox for hook
            self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
            self.checkBox.setText("")
            self.checkBox.setObjectName("checkBox")
            self.gridLayout_3.addWidget(self.checkBox, rowNum, 0, 1, 1)
            #adds the hook name
            self.hookNameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.hookNameLabel.setObjectName("label_4")
            self.gridLayout_3.addWidget(self.hookNameLabel, rowNum, 1, 1, 1)
            self.hookNameLabel.setText(h.getName())
            #adds the hook enable/disable option
            self.comboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
            self.comboBox.setObjectName("comboBox")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.comboBox.setItemText(1, "Enabled")
            self.comboBox.setItemText(2, "Disabled")
            self.comboBox.setItemText(0, "Enabled/Disabled")
            self.gridLayout_3.addWidget(self.comboBox, rowNum, 3, 1, 1)
            #add the sequence number edit box
            self.seqEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            self.seqEdit.setObjectName("seqEdit")
            self.seqEdit.setPlaceholderText("Enter Sequence No.")
            self.gridLayout_3.addWidget(self.seqEdit, rowNum, 5, 1, 1)
            
            rowNum+=1 #to the next row!

        return


    

    


if __name__ == "__main__":
    import sys
    from HookFunction.Hook import Hook
    from HookFunction.HookCollection import HookCollection
    from HookFunction.HookCollectionManager import HookCollectionManager

    

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    manager = ui.manager
    ui.setupUi(Dialog,manager)
    ui.updateHookBox()
    Dialog.show()
    sys.exit(app.exec_())
