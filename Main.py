# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from CreateEditHookOverlay import Ui_CreateEditHook as CreateEditHook
from CreateEditHookCollectionOverlay import Ui_Dialog as CreateEditHookCollection
from MessageBasedOverlay import Ui_Dialog as OkDialog
from Proxy import Proxy
import threading
from kamene.all import *
from HookFunction.Hook import Hook
from HookFunction.HookCollection import HookCollection
from HookFunction.HookCollectionManager import HookCollectionManager
from rules import rules

class Ui_MainWindow(object):

    manager = HookCollectionManager([],[])
    rulesP = rules()
    queue_size = 100
    captureFilterExpression = ""
    count = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1139, 796)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.StackView = QtWidgets.QStackedWidget(self.centralwidget)
        self.StackView.setObjectName("StackView")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.HV_GroupBox_2 = QtWidgets.QGroupBox(self.page)
        self.HV_GroupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.HV_GroupBox_2.setObjectName("HV_GroupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.HV_GroupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.HV_TopContentFrame_2 = QtWidgets.QFrame(self.HV_GroupBox_2)
        self.HV_TopContentFrame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.HV_TopContentFrame_2.setObjectName("HV_TopContentFrame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.HV_TopContentFrame_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4.addWidget(self.HV_TopContentFrame_2)
        self.gridLayout_15.addWidget(self.HV_GroupBox_2, 0, 0, 1, 1)
        self.StackView.addWidget(self.page)

        # Hook View
        self.HookView = QtWidgets.QWidget()
        self.HookView.setObjectName("HookView")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.HookView)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.HV_GroupBox = QtWidgets.QGroupBox(self.HookView)

        self.HV_GroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.HV_GroupBox.setObjectName("HV_GroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.HV_GroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.HV_TopContentFrame = QtWidgets.QFrame(self.HV_GroupBox)

        #Setting format for frame in Hook View
        self.HV_TopContentFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.HV_TopContentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HV_TopContentFrame.setObjectName("HV_TopContentFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.HV_TopContentFrame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.HV_TC_AddHookButton = QtWidgets.QPushButton(self.HV_TopContentFrame)
        self.HV_TC_AddHookButton.setObjectName("HV_TC_AddHookButton")
        self.horizontalLayout_5.addWidget(self.HV_TC_AddHookButton)
        self.HV_TC_EditButton = QtWidgets.QPushButton(self.HV_TopContentFrame)
        self.HV_TC_EditButton.setObjectName("HV_TC_EditButton")
        self.horizontalLayout_5.addWidget(self.HV_TC_EditButton)
        self.HV_TC_DeleteButton = QtWidgets.QPushButton(self.HV_TopContentFrame)
        self.HV_TC_DeleteButton.setObjectName("HV_TC_DeleteButton")
        self.horizontalLayout_5.addWidget(self.HV_TC_DeleteButton)
        spacerItem = QtWidgets.QSpacerItem(320, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.HV_TC_SearchLabel = QtWidgets.QLabel(self.HV_TopContentFrame)
        self.HV_TC_SearchLabel.setObjectName("HV_TC_SearchLabel")
        self.horizontalLayout_5.addWidget(self.HV_TC_SearchLabel)
        self.HV_TC_TextBox = QtWidgets.QLineEdit(self.HV_TopContentFrame)
        self.HV_TC_TextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.HV_TC_TextBox.setObjectName("HV_TC_TextBox")
        self.horizontalLayout_5.addWidget(self.HV_TC_TextBox)
        self.verticalLayout_3.addWidget(self.HV_TopContentFrame)

        self.HV_HookPropertiesGroupBox = QtWidgets.QGroupBox(self.HV_GroupBox)
        self.HV_HookPropertiesGroupBox.setEnabled(True)
        self.HV_HookPropertiesGroupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.HV_HookPropertiesGroupBox.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.HV_HookPropertiesGroupBox.setFont(font)
        self.HV_HookPropertiesGroupBox.setAutoFillBackground(False)
        self.HV_HookPropertiesGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.HV_HookPropertiesGroupBox.setFlat(False)
        self.HV_HookPropertiesGroupBox.setProperty("columnWidth", "")
        self.HV_HookPropertiesGroupBox.setObjectName("HV_HookPropertiesGroupBox")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.HV_HookPropertiesGroupBox)
        self.gridLayout_19.setObjectName("gridLayout_19")

        #Singular hooks (bottom box in HookCollection window)
        self.HV_HP_HookTreeView = QtWidgets.QTreeWidget(self.HV_HookPropertiesGroupBox)
        self.HV_HP_HookTreeView.setObjectName("HV_HP_HookTreeView") #Tree view for hook items
        self.HV_HP_HookTreeView.headerItem().setTextAlignment(0, QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.HV_HP_HookTreeView.headerItem().setTextAlignment(1, QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.HV_HP_HookTreeView.headerItem().setTextAlignment(2, QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)

        item_0 = QtWidgets.QTreeWidgetItem(self.HV_HP_HookTreeView)
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        item_0 = QtWidgets.QTreeWidgetItem(self.HV_HP_HookTreeView)
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        self.HV_HP_HookTreeView.header().setCascadingSectionResizes(False)
        self.HV_HP_HookTreeView.header().setDefaultSectionSize(250)
        self.gridLayout_19.addWidget(self.HV_HP_HookTreeView, 0, 0, 1, 2)
        #end of singular hook section 1#

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem2, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.HV_HookPropertiesGroupBox)
        self.gridLayout_17.addWidget(self.HV_GroupBox, 0, 1, 1, 1)
        self.StackView.addWidget(self.HookView)

        ###HOOK COLLECTION VIEW###
        ##Group box formatting (placement of top and bottom boxes and buttons)
        self.HookCollectionView = QtWidgets.QWidget()
        self.HookCollectionView.setObjectName("HookCollectionView")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.HookCollectionView)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.GroupBox_HCV = QtWidgets.QGroupBox(self.HookCollectionView)
        self.GroupBox_HCV.setAlignment(QtCore.Qt.AlignCenter)
        self.GroupBox_HCV.setObjectName("GroupBox_HCV")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.GroupBox_HCV)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Frame_TopContent = QtWidgets.QFrame(self.GroupBox_HCV)
        self.Frame_TopContent.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Frame_TopContent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_TopContent.setObjectName("Frame_TopContent")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.Frame_TopContent)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.Button_AddHookCollection = QtWidgets.QPushButton(self.Frame_TopContent)
        self.Button_AddHookCollection.setObjectName("Button_AddHookCollection")
        self.horizontalLayout_11.addWidget(self.Button_AddHookCollection)
        self.Button_Edit = QtWidgets.QPushButton(self.Frame_TopContent)
        self.Button_Edit.setObjectName("Button_Edit")
        self.horizontalLayout_11.addWidget(self.Button_Edit)
        self.Button_Delete = QtWidgets.QPushButton(self.Frame_TopContent)
        self.Button_Delete.setObjectName("Button_Delete")
        self.horizontalLayout_11.addWidget(self.Button_Delete)
        spacerItem3 = QtWidgets.QSpacerItem(320, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.Label_Search = QtWidgets.QLabel(self.Frame_TopContent)
        self.Label_Search.setObjectName("Label_Search")
        self.horizontalLayout_11.addWidget(self.Label_Search)
        self.TextBox_Search = QtWidgets.QLineEdit(self.Frame_TopContent)
        self.TextBox_Search.setAlignment(QtCore.Qt.AlignCenter)
        self.TextBox_Search.setObjectName("TextBox_Search")
        self.horizontalLayout_11.addWidget(self.TextBox_Search)
        self.verticalLayout_2.addWidget(self.Frame_TopContent)
        self.HCV_HookCollectionProperties_GroupBox = QtWidgets.QGroupBox(self.GroupBox_HCV)
        self.HCV_HookCollectionProperties_GroupBox.setEnabled(True)
        self.HCV_HookCollectionProperties_GroupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.HCV_HookCollectionProperties_GroupBox.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.HCV_HookCollectionProperties_GroupBox.setFont(font)
        self.HCV_HookCollectionProperties_GroupBox.setAutoFillBackground(False)
        self.HCV_HookCollectionProperties_GroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.HCV_HookCollectionProperties_GroupBox.setFlat(False)
        self.HCV_HookCollectionProperties_GroupBox.setProperty("columnWidth", "")
        self.HCV_HookCollectionProperties_GroupBox.setObjectName("HCV_HookCollectionProperties_GroupBox")
        self.gridLayout_34 = QtWidgets.QGridLayout(self.HCV_HookCollectionProperties_GroupBox)
        self.gridLayout_34.setObjectName("gridLayout_34")
        #End Group box formatting
        
        #Hook collection Tree STRUCTURE (Top box in Hook Collection View - the actual hook collection content is NOT set here.)
        self.HCV_HCP_TreeView = QtWidgets.QTreeWidget(self.HCV_HookCollectionProperties_GroupBox)
        self.HCV_HCP_TreeView.setObjectName("HCV_HCP_TreeView")
        #The header placement for the Hook Collection box is set here
        self.HCV_HCP_TreeView.headerItem().setTextAlignment(0, QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.HCV_HCP_TreeView.headerItem().setTextAlignment(1, QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.HCV_HCP_TreeView.headerItem().setTextAlignment(2, QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.HCV_HCP_TreeView.headerItem().setTextAlignment(3, QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        
        self.HCV_HCP_TreeView.header().setCascadingSectionResizes(False)
        self.HCV_HCP_TreeView.header().setDefaultSectionSize(250)
        self.gridLayout_34.addWidget(self.HCV_HCP_TreeView, 0, 0, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_34.addItem(spacerItem4, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_34.addItem(spacerItem5, 2, 1, 1, 1)
        self.HCV_HookProperties_GroupBox = QtWidgets.QGroupBox(self.HCV_HookCollectionProperties_GroupBox)
        self.HCV_HookProperties_GroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.HCV_HookProperties_GroupBox.setObjectName("HCV_HookProperties_GroupBox")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.HCV_HookProperties_GroupBox)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        #end header placement


        self.gridLayout_34.addWidget(self.HCV_HookProperties_GroupBox, 1, 0, 1, 2)
        self.verticalLayout_2.addWidget(self.HCV_HookCollectionProperties_GroupBox)
        self.gridLayout_13.addWidget(self.GroupBox_HCV, 1, 0, 1, 1)
        self.StackView.addWidget(self.HookCollectionView)
        
        ###END OF HOOK COLLECTION VIEW###

        # Live Packet View
        self.LivePacketView = QtWidgets.QWidget()
        self.LivePacketView.setObjectName("LivePacketView")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.LivePacketView)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.LPV_GroupBox_LivePacketView = QtWidgets.QGroupBox(self.LivePacketView)
        self.LPV_GroupBox_LivePacketView.setAlignment(QtCore.Qt.AlignCenter)
        self.LPV_GroupBox_LivePacketView.setObjectName("LPV_GroupBox_LivePacketView")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.LPV_GroupBox_LivePacketView)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.LPV_Frame_FieldArea = QtWidgets.QFrame(self.LPV_GroupBox_LivePacketView)
        self.LPV_Frame_FieldArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LPV_Frame_FieldArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LPV_Frame_FieldArea.setObjectName("LPV_Frame_FieldArea")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.LPV_Frame_FieldArea)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.LPV_Table_FieldArea = QtWidgets.QTableWidget(self.LPV_Frame_FieldArea)
        self.LPV_Table_FieldArea.setObjectName("LPV_Table_FieldArea")
        self.LPV_Table_FieldArea.setColumnCount(4)
        self.LPV_Table_FieldArea.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.LPV_Table_FieldArea.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.LPV_Table_FieldArea.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.LPV_Table_FieldArea.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.LPV_Table_FieldArea.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.LPV_Table_FieldArea.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.LPV_Table_FieldArea.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.LPV_Table_FieldArea.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.LPV_Table_FieldArea.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.LPV_Table_FieldArea.setHorizontalHeaderItem(3, item)
        self.gridLayout_6.addWidget(self.LPV_Table_FieldArea, 1, 0, 1, 4)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem6, 3, 0, 1, 1)
        self.LPV_Button_ShowModification = QtWidgets.QPushButton(self.LPV_Frame_FieldArea)
        self.LPV_Button_ShowModification.setObjectName("LPV_Button_ShowModification")
        self.gridLayout_6.addWidget(self.LPV_Button_ShowModification, 3, 1, 1, 1)
        self.LPV_Button_Forward = QtWidgets.QPushButton(self.LPV_Frame_FieldArea)
        self.LPV_Button_Forward.setObjectName("LPV_Button_Forward")
        self.gridLayout_6.addWidget(self.LPV_Button_Forward, 3, 2, 1, 1)
        self.LPV_Button_Drop = QtWidgets.QPushButton(self.LPV_Frame_FieldArea)
        self.LPV_Button_Drop.setObjectName("LPV_Button_Drop")
        self.gridLayout_6.addWidget(self.LPV_Button_Drop, 3, 3, 1, 1)
        self.LPV_Label_FieldArea = QtWidgets.QLabel(self.LPV_Frame_FieldArea)
        self.LPV_Label_FieldArea.setObjectName("LPV_Label_FieldArea")
        self.gridLayout_6.addWidget(self.LPV_Label_FieldArea, 0, 0, 1, 4)
        self.LPV_Label_InformationalText = QtWidgets.QLabel(self.LPV_Frame_FieldArea)
        self.LPV_Label_InformationalText.setObjectName("LPV_Label_InformationalText")
        self.gridLayout_6.addWidget(self.LPV_Label_InformationalText, 2, 0, 1, 2)
        self.gridLayout_3.addWidget(self.LPV_Frame_FieldArea, 3, 0, 1, 1)
        self.LPV_Frame_FuzzingArea = QtWidgets.QFrame(self.LPV_GroupBox_LivePacketView)
        self.LPV_Frame_FuzzingArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LPV_Frame_FuzzingArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LPV_Frame_FuzzingArea.setObjectName("LPV_Frame_FuzzingArea")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.LPV_Frame_FuzzingArea)
        self.gridLayout_16.setObjectName("gridLayout_16")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_16.addItem(spacerItem7, 7, 1, 1, 1)
        self.LPV_Line_H = QtWidgets.QFrame(self.LPV_Frame_FuzzingArea)
        self.LPV_Line_H.setFrameShape(QtWidgets.QFrame.HLine)
        self.LPV_Line_H.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LPV_Line_H.setObjectName("LPV_Line_H")
        self.gridLayout_16.addWidget(self.LPV_Line_H, 1, 0, 1, 3)
        self.LPV_TextBox_ReturnType = QtWidgets.QLineEdit(self.LPV_Frame_FuzzingArea)
        self.LPV_TextBox_ReturnType.setAlignment(QtCore.Qt.AlignCenter)
        self.LPV_TextBox_ReturnType.setObjectName("LPV_TextBox_ReturnType")
        self.gridLayout_16.addWidget(self.LPV_TextBox_ReturnType, 4, 1, 1, 2)
        self.LPV_Label_FuzzingArea = QtWidgets.QLabel(self.LPV_Frame_FuzzingArea)
        self.LPV_Label_FuzzingArea.setObjectName("LPV_Label_FuzzingArea")
        self.gridLayout_16.addWidget(self.LPV_Label_FuzzingArea, 0, 0, 1, 3)
        self.LPV_Button_Stop = QtWidgets.QPushButton(self.LPV_Frame_FuzzingArea)
        self.LPV_Button_Stop.setObjectName("LPV_Button_Stop")
        self.gridLayout_16.addWidget(self.LPV_Button_Stop, 8, 2, 1, 1)
        self.LPV_Label_Minimum = QtWidgets.QLabel(self.LPV_Frame_FuzzingArea)
        self.LPV_Label_Minimum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LPV_Label_Minimum.setObjectName("LPV_Label_Minimum")
        self.gridLayout_16.addWidget(self.LPV_Label_Minimum, 5, 0, 1, 1)
        self.LPV_Label_PacketName = QtWidgets.QLabel(self.LPV_Frame_FuzzingArea)
        self.LPV_Label_PacketName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LPV_Label_PacketName.setObjectName("LPV_Label_PacketName")
        self.gridLayout_16.addWidget(self.LPV_Label_PacketName, 2, 0, 1, 1)
        self.LPV_Label_Maximum = QtWidgets.QLabel(self.LPV_Frame_FuzzingArea)
        self.LPV_Label_Maximum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LPV_Label_Maximum.setObjectName("LPV_Label_Maximum")
        self.gridLayout_16.addWidget(self.LPV_Label_Maximum, 6, 0, 1, 1)
        self.LPV_Label_ReturnType = QtWidgets.QLabel(self.LPV_Frame_FuzzingArea)
        self.LPV_Label_ReturnType.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LPV_Label_ReturnType.setObjectName("LPV_Label_ReturnType")
        self.gridLayout_16.addWidget(self.LPV_Label_ReturnType, 4, 0, 1, 1)
        self.LPV_TextBox_Maximum = QtWidgets.QLineEdit(self.LPV_Frame_FuzzingArea)
        self.LPV_TextBox_Maximum.setAlignment(QtCore.Qt.AlignCenter)
        self.LPV_TextBox_Maximum.setObjectName("LPV_TextBox_Maximum")
        self.gridLayout_16.addWidget(self.LPV_TextBox_Maximum, 6, 1, 1, 2)
        self.LPV_TextBox_FieldName = QtWidgets.QLineEdit(self.LPV_Frame_FuzzingArea)
        self.LPV_TextBox_FieldName.setAlignment(QtCore.Qt.AlignCenter)
        self.LPV_TextBox_FieldName.setObjectName("LPV_TextBox_FieldName")
        self.gridLayout_16.addWidget(self.LPV_TextBox_FieldName, 3, 1, 1, 2)
        self.LPV_TextBox_PacketName = QtWidgets.QLineEdit(self.LPV_Frame_FuzzingArea)
        self.LPV_TextBox_PacketName.setAlignment(QtCore.Qt.AlignCenter)
        self.LPV_TextBox_PacketName.setObjectName("LPV_TextBox_PacketName")
        self.gridLayout_16.addWidget(self.LPV_TextBox_PacketName, 2, 1, 1, 2)
        self.LPV_Button_Fuzz = QtWidgets.QPushButton(self.LPV_Frame_FuzzingArea)
        self.LPV_Button_Fuzz.setObjectName("LPV_Button_Fuzz")
        self.gridLayout_16.addWidget(self.LPV_Button_Fuzz, 8, 1, 1, 1)
        self.LPV_Label_FieldName = QtWidgets.QLabel(self.LPV_Frame_FuzzingArea)
        self.LPV_Label_FieldName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LPV_Label_FieldName.setObjectName("LPV_Label_FieldName")
        self.gridLayout_16.addWidget(self.LPV_Label_FieldName, 3, 0, 1, 1)
        self.LPV_TextBox_Minimum = QtWidgets.QLineEdit(self.LPV_Frame_FuzzingArea)
        self.LPV_TextBox_Minimum.setAlignment(QtCore.Qt.AlignCenter)
        self.LPV_TextBox_Minimum.setObjectName("LPV_TextBox_Minimum")
        self.gridLayout_16.addWidget(self.LPV_TextBox_Minimum, 5, 1, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem8, 8, 0, 1, 1)
        self.gridLayout_3.addWidget(self.LPV_Frame_FuzzingArea, 3, 1, 1, 1)
        self.LPV_Frame_PacketArea = QtWidgets.QFrame(self.LPV_GroupBox_LivePacketView)
        self.LPV_Frame_PacketArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LPV_Frame_PacketArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LPV_Frame_PacketArea.setObjectName("LPV_Frame_PacketArea")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.LPV_Frame_PacketArea)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.LPV_Label_PacketArea = QtWidgets.QLabel(self.LPV_Frame_PacketArea)
        self.LPV_Label_PacketArea.setObjectName("LPV_Label_PacketArea")
        self.gridLayout_5.addWidget(self.LPV_Label_PacketArea, 0, 0, 1, 1)
        self.LPV_Button_Clear_2 = QtWidgets.QPushButton(self.LPV_Frame_PacketArea)
        self.LPV_Button_Clear_2.setObjectName("LPV_Button_Clear_2")
        self.gridLayout_5.addWidget(self.LPV_Button_Clear_2, 2, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem9, 1, 1, 1, 1)
        self.LPV_TabView_PacketArea = QtWidgets.QTabWidget(self.LPV_Frame_PacketArea)
        self.LPV_TabView_PacketArea.setObjectName("LPV_TabView_PacketArea")
        self.LPV_Tab_Dissected = QtWidgets.QWidget()
        self.LPV_Tab_Dissected.setObjectName("LPV_Tab_Dissected")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.LPV_Tab_Dissected)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LPV_TreeView_Dissected = QtWidgets.QTreeWidget(self.LPV_Tab_Dissected)
        self.LPV_TreeView_Dissected.setObjectName("LPV_TreeView_Dissected")



        self.horizontalLayout_2.addWidget(self.LPV_TreeView_Dissected)
        self.LPV_TabView_PacketArea.addTab(self.LPV_Tab_Dissected, "")
        self.LPV_Tab_Binary = QtWidgets.QWidget()
        self.LPV_Tab_Binary.setObjectName("LPV_Tab_Binary")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.LPV_Tab_Binary)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.LPV_ListView_Binary = QtWidgets.QListWidget(self.LPV_Tab_Binary)
        self.LPV_ListView_Binary.setObjectName("LPV_ListView_Binary")




        self.gridLayout_22.addWidget(self.LPV_ListView_Binary, 0, 0, 1, 1)
        self.LPV_TabView_PacketArea.addTab(self.LPV_Tab_Binary, "")
        self.LPV_Tab_HEX = QtWidgets.QWidget()
        self.LPV_Tab_HEX.setObjectName("LPV_Tab_HEX")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.LPV_Tab_HEX)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.LPV_ListView_HEX = QtWidgets.QListWidget(self.LPV_Tab_HEX)
        self.LPV_ListView_HEX.setObjectName("LPV_ListView_HEX")
        item = QtWidgets.QListWidgetItem()
        self.LPV_ListView_HEX.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.LPV_ListView_HEX.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.LPV_ListView_HEX.addItem(item)
        self.gridLayout_23.addWidget(self.LPV_ListView_HEX, 0, 0, 1, 1)
        self.LPV_TabView_PacketArea.addTab(self.LPV_Tab_HEX, "")
        self.gridLayout_5.addWidget(self.LPV_TabView_PacketArea, 1, 0, 2, 1)
        self.gridLayout_3.addWidget(self.LPV_Frame_PacketArea, 2, 0, 1, 2)
        self.LPV_Frame_CaptureFilter = QtWidgets.QFrame(self.LPV_GroupBox_LivePacketView)
        self.LPV_Frame_CaptureFilter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LPV_Frame_CaptureFilter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LPV_Frame_CaptureFilter.setObjectName("LPV_Frame_CaptureFilter")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.LPV_Frame_CaptureFilter)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.LPV_Label_Filter = QtWidgets.QLabel(self.LPV_Frame_CaptureFilter)
        self.LPV_Label_Filter.setObjectName("LPV_Label_Filter")
        self.gridLayout_4.addWidget(self.LPV_Label_Filter, 1, 0, 1, 1)
        self.LPV_TextBox_FilterExpression = QtWidgets.QLineEdit(self.LPV_Frame_CaptureFilter)
        self.LPV_TextBox_FilterExpression.setAlignment(QtCore.Qt.AlignCenter)
        self.LPV_TextBox_FilterExpression.setObjectName("LPV_TextBox_FilterExpression")
        self.gridLayout_4.addWidget(self.LPV_TextBox_FilterExpression, 1, 1, 1, 1)
        self.LPV_Label_CaptureFilter = QtWidgets.QLabel(self.LPV_Frame_CaptureFilter)
        self.LPV_Label_CaptureFilter.setObjectName("LPV_Label_CaptureFilter")
        self.gridLayout_4.addWidget(self.LPV_Label_CaptureFilter, 0, 0, 1, 4)
        self.LPV_Button_Apply = QtWidgets.QPushButton(self.LPV_Frame_CaptureFilter)
        self.LPV_Button_Apply.setObjectName("LPV_Button_Apply")

        self.LPV_Button_Apply.clicked.connect(lambda: self.setCaptureFilter(self.LPV_TextBox_FilterExpression))

        self.gridLayout_4.addWidget(self.LPV_Button_Apply, 1, 2, 1, 1)
        self.LPV_Button_Clear = QtWidgets.QPushButton(self.LPV_Frame_CaptureFilter)
        self.LPV_Button_Clear.setObjectName("LPV_Button_Clear")
        self.gridLayout_4.addWidget(self.LPV_Button_Clear, 1, 3, 1, 1)
        self.gridLayout_3.addWidget(self.LPV_Frame_CaptureFilter, 1, 0, 1, 2)
        self.LPV_Frame_TopContent = QtWidgets.QFrame(self.LPV_GroupBox_LivePacketView)
        self.LPV_Frame_TopContent.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LPV_Frame_TopContent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LPV_Frame_TopContent.setObjectName("LPV_Frame_TopContent")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.LPV_Frame_TopContent)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LPV_Label_ProxyBehavior = QtWidgets.QLabel(self.LPV_Frame_TopContent)
        self.LPV_Label_ProxyBehavior.setObjectName("LPV_Label_ProxyBehavior")
        self.horizontalLayout.addWidget(self.LPV_Label_ProxyBehavior)
        self.LPV_ComboBox_ProxyBehavior = QtWidgets.QComboBox(self.LPV_Frame_TopContent)
        self.LPV_ComboBox_ProxyBehavior.setObjectName("LPV_ComboBox_ProxyBehavior")
        self.LPV_ComboBox_ProxyBehavior.addItem("")
        self.LPV_ComboBox_ProxyBehavior.addItem("")
        self.horizontalLayout.addWidget(self.LPV_ComboBox_ProxyBehavior)
        self.LPV_Label_InterceptionBehavior = QtWidgets.QLabel(self.LPV_Frame_TopContent)
        self.LPV_Label_InterceptionBehavior.setObjectName("LPV_Label_InterceptionBehavior")
        self.horizontalLayout.addWidget(self.LPV_Label_InterceptionBehavior)
        self.LPV_ComboBox_InterceptionBehavior = QtWidgets.QComboBox(self.LPV_Frame_TopContent)
        self.LPV_ComboBox_InterceptionBehavior.setObjectName("LPV_ComboBox_InterceptionBehavior")
        self.LPV_ComboBox_InterceptionBehavior.addItem("")
        self.LPV_ComboBox_InterceptionBehavior.addItem("")
        self.LPV_ComboBox_InterceptionBehavior.setDisabled(True)
        self.horizontalLayout.addWidget(self.LPV_ComboBox_InterceptionBehavior)
        self.LPV_Label_QueueSize = QtWidgets.QLabel(self.LPV_Frame_TopContent)
        self.LPV_Label_QueueSize.setObjectName("LPV_Label_QueueSize")
        self.horizontalLayout.addWidget(self.LPV_Label_QueueSize)
        self.LPV_TextBox_QueueSize = QtWidgets.QLineEdit(self.LPV_Frame_TopContent)
        self.LPV_TextBox_QueueSize.setAlignment(QtCore.Qt.AlignCenter)
        self.LPV_TextBox_QueueSize.setObjectName("LPV_TextBox_QueueSize")
        self.LPV_TextBox_QueueSize.setDisabled(True)
        self.horizontalLayout.addWidget(self.LPV_TextBox_QueueSize)
        self.gridLayout_3.addWidget(self.LPV_Frame_TopContent, 0, 0, 1, 2)
        self.gridLayout_2.addWidget(self.LPV_GroupBox_LivePacketView, 0, 0, 1, 1)
        self.StackView.addWidget(self.LivePacketView)

        # PCAP View
        self.PacketFromPCAPView = QtWidgets.QWidget()
        self.PacketFromPCAPView.setObjectName("PacketFromPCAPView")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.PacketFromPCAPView)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.PFP_GroupBox_PacketFromPCAPView = QtWidgets.QGroupBox(self.PacketFromPCAPView)
        self.PFP_GroupBox_PacketFromPCAPView.setAlignment(QtCore.Qt.AlignCenter)
        self.PFP_GroupBox_PacketFromPCAPView.setObjectName("PFP_GroupBox_PacketFromPCAPView")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.PFP_GroupBox_PacketFromPCAPView)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.PFP_CaptureFilter = QtWidgets.QFrame(self.PFP_GroupBox_PacketFromPCAPView)
        self.PFP_CaptureFilter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PFP_CaptureFilter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PFP_CaptureFilter.setObjectName("PFP_CaptureFilter")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.PFP_CaptureFilter)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.PFP_Label_Filter = QtWidgets.QLabel(self.PFP_CaptureFilter)
        self.PFP_Label_Filter.setObjectName("PFP_Label_Filter")
        self.gridLayout_8.addWidget(self.PFP_Label_Filter, 1, 0, 1, 1)
        self.PFP_TextBox_FilterExpression = QtWidgets.QLineEdit(self.PFP_CaptureFilter)
        self.PFP_TextBox_FilterExpression.setAlignment(QtCore.Qt.AlignCenter)
        self.PFP_TextBox_FilterExpression.setObjectName("PFP_TextBox_FilterExpression")
        self.gridLayout_8.addWidget(self.PFP_TextBox_FilterExpression, 1, 1, 1, 1)
        self.PFP_Label_CaptureFilter = QtWidgets.QLabel(self.PFP_CaptureFilter)
        self.PFP_Label_CaptureFilter.setObjectName("PFP_Label_CaptureFilter")
        self.gridLayout_8.addWidget(self.PFP_Label_CaptureFilter, 0, 0, 1, 4)
        self.PFP_Button_Apply = QtWidgets.QPushButton(self.PFP_CaptureFilter)
        self.PFP_Button_Apply.setObjectName("PFP_Button_Apply")
        self.gridLayout_8.addWidget(self.PFP_Button_Apply, 1, 2, 1, 1)
        self.PFP_Button_Clear_2 = QtWidgets.QPushButton(self.PFP_CaptureFilter)
        self.PFP_Button_Clear_2.setObjectName("PFP_Button_Clear_2")
        self.gridLayout_8.addWidget(self.PFP_Button_Clear_2, 1, 3, 1, 1)
        self.gridLayout_7.addWidget(self.PFP_CaptureFilter, 1, 0, 1, 2)
        self.PFP_Frame_FuzzingArea = QtWidgets.QFrame(self.PFP_GroupBox_PacketFromPCAPView)
        self.PFP_Frame_FuzzingArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PFP_Frame_FuzzingArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PFP_Frame_FuzzingArea.setObjectName("PFP_Frame_FuzzingArea")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.PFP_Frame_FuzzingArea)
        self.gridLayout_18.setObjectName("gridLayout_18")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_18.addItem(spacerItem10, 7, 1, 1, 1)
        self.PFP_Line_Fuzz = QtWidgets.QFrame(self.PFP_Frame_FuzzingArea)
        self.PFP_Line_Fuzz.setFrameShape(QtWidgets.QFrame.HLine)
        self.PFP_Line_Fuzz.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.PFP_Line_Fuzz.setObjectName("PFP_Line_Fuzz")
        self.gridLayout_18.addWidget(self.PFP_Line_Fuzz, 1, 0, 1, 3)
        self.PFP_Textbox_ReturnType = QtWidgets.QLineEdit(self.PFP_Frame_FuzzingArea)
        self.PFP_Textbox_ReturnType.setAlignment(QtCore.Qt.AlignCenter)
        self.PFP_Textbox_ReturnType.setObjectName("PFP_Textbox_ReturnType")
        self.gridLayout_18.addWidget(self.PFP_Textbox_ReturnType, 4, 1, 1, 2)
        self.PFP_Label_FuzzingArea = QtWidgets.QLabel(self.PFP_Frame_FuzzingArea)
        self.PFP_Label_FuzzingArea.setObjectName("PFP_Label_FuzzingArea")
        self.gridLayout_18.addWidget(self.PFP_Label_FuzzingArea, 0, 0, 1, 3)
        self.PFP_Button_Stop = QtWidgets.QPushButton(self.PFP_Frame_FuzzingArea)
        self.PFP_Button_Stop.setObjectName("PFP_Button_Stop")
        self.gridLayout_18.addWidget(self.PFP_Button_Stop, 8, 2, 1, 1)
        self.PFP_Label_Minimum = QtWidgets.QLabel(self.PFP_Frame_FuzzingArea)
        self.PFP_Label_Minimum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PFP_Label_Minimum.setObjectName("PFP_Label_Minimum")
        self.gridLayout_18.addWidget(self.PFP_Label_Minimum, 5, 0, 1, 1)
        self.PFP_Label_SelectedPacketName = QtWidgets.QLabel(self.PFP_Frame_FuzzingArea)
        self.PFP_Label_SelectedPacketName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PFP_Label_SelectedPacketName.setObjectName("PFP_Label_SelectedPacketName")
        self.gridLayout_18.addWidget(self.PFP_Label_SelectedPacketName, 2, 0, 1, 1)
        self.PFP_Label_Maximum = QtWidgets.QLabel(self.PFP_Frame_FuzzingArea)
        self.PFP_Label_Maximum.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PFP_Label_Maximum.setObjectName("PFP_Label_Maximum")
        self.gridLayout_18.addWidget(self.PFP_Label_Maximum, 6, 0, 1, 1)
        self.PFP_Label_ReturnType = QtWidgets.QLabel(self.PFP_Frame_FuzzingArea)
        self.PFP_Label_ReturnType.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PFP_Label_ReturnType.setObjectName("PFP_Label_ReturnType")
        self.gridLayout_18.addWidget(self.PFP_Label_ReturnType, 4, 0, 1, 1)
        self.PFP_Textbox_Maximum = QtWidgets.QLineEdit(self.PFP_Frame_FuzzingArea)
        self.PFP_Textbox_Maximum.setAlignment(QtCore.Qt.AlignCenter)
        self.PFP_Textbox_Maximum.setObjectName("PFP_Textbox_Maximum")
        self.gridLayout_18.addWidget(self.PFP_Textbox_Maximum, 6, 1, 1, 2)
        self.PFP_Textbox_FieldName = QtWidgets.QLineEdit(self.PFP_Frame_FuzzingArea)
        self.PFP_Textbox_FieldName.setAlignment(QtCore.Qt.AlignCenter)
        self.PFP_Textbox_FieldName.setObjectName("PFP_Textbox_FieldName")
        self.gridLayout_18.addWidget(self.PFP_Textbox_FieldName, 3, 1, 1, 2)
        self.PFP_Textbox_PacketName = QtWidgets.QLineEdit(self.PFP_Frame_FuzzingArea)
        self.PFP_Textbox_PacketName.setAlignment(QtCore.Qt.AlignCenter)
        self.PFP_Textbox_PacketName.setObjectName("PFP_Textbox_PacketName")
        self.gridLayout_18.addWidget(self.PFP_Textbox_PacketName, 2, 1, 1, 2)
        self.PFP_Button_Fuzz = QtWidgets.QPushButton(self.PFP_Frame_FuzzingArea)
        self.PFP_Button_Fuzz.setObjectName("PFP_Button_Fuzz")
        self.gridLayout_18.addWidget(self.PFP_Button_Fuzz, 8, 1, 1, 1)
        self.PFP_Label_FieldName = QtWidgets.QLabel(self.PFP_Frame_FuzzingArea)
        self.PFP_Label_FieldName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PFP_Label_FieldName.setObjectName("PFP_Label_FieldName")
        self.gridLayout_18.addWidget(self.PFP_Label_FieldName, 3, 0, 1, 1)
        self.PFP_Textbox_Minimum = QtWidgets.QLineEdit(self.PFP_Frame_FuzzingArea)
        self.PFP_Textbox_Minimum.setAlignment(QtCore.Qt.AlignCenter)
        self.PFP_Textbox_Minimum.setObjectName("PFP_Textbox_Minimum")
        self.gridLayout_18.addWidget(self.PFP_Textbox_Minimum, 5, 1, 1, 2)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem11, 8, 0, 1, 1)
        self.gridLayout_7.addWidget(self.PFP_Frame_FuzzingArea, 3, 1, 1, 1)
        self.PFP_Frame_PacketArea = QtWidgets.QFrame(self.PFP_GroupBox_PacketFromPCAPView)
        self.PFP_Frame_PacketArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PFP_Frame_PacketArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PFP_Frame_PacketArea.setObjectName("PFP_Frame_PacketArea")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.PFP_Frame_PacketArea)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.PFP_Label_PacketArea = QtWidgets.QLabel(self.PFP_Frame_PacketArea)
        self.PFP_Label_PacketArea.setObjectName("PFP_Label_PacketArea")
        self.gridLayout_9.addWidget(self.PFP_Label_PacketArea, 0, 0, 1, 1)
        self.PFP_Button_Clear = QtWidgets.QPushButton(self.PFP_Frame_PacketArea)
        self.PFP_Button_Clear.setObjectName("PFP_Button_Clear")
        self.gridLayout_9.addWidget(self.PFP_Button_Clear, 2, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem12, 1, 1, 1, 1)
        self.PFP_TabView_PacketArea = QtWidgets.QTabWidget(self.PFP_Frame_PacketArea)
        self.PFP_TabView_PacketArea.setObjectName("PFP_TabView_PacketArea")
        self.PFP_Tab_Dissected = QtWidgets.QWidget()
        self.PFP_Tab_Dissected.setObjectName("PFP_Tab_Dissected")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.PFP_Tab_Dissected)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.PFP_TreeView_Dissected = QtWidgets.QTreeWidget(self.PFP_Tab_Dissected)
        self.PFP_TreeView_Dissected.setObjectName("PFP_TreeView_Dissected")



        self.PFP_TabView_PacketArea.addTab(self.PFP_Tab_Dissected, "")
        self.PFP_Tab_Binary = QtWidgets.QWidget()
        self.PFP_Tab_Binary.setObjectName("PFP_Tab_Binary")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.PFP_Tab_Binary)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.PFP_ListView_Binary = QtWidgets.QListWidget(self.PFP_Tab_Binary)
        self.PFP_ListView_Binary.setObjectName("PFP_ListView_Binary")
        



        self.gridLayout_20.addWidget(self.PFP_ListView_Binary, 0, 0, 1, 1)
        self.PFP_TabView_PacketArea.addTab(self.PFP_Tab_Binary, "")
        self.PFP_Tab_HEX = QtWidgets.QWidget()
        self.PFP_Tab_HEX.setObjectName("PFP_Tab_HEX")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.PFP_Tab_HEX)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.PFP_ListView_HEX = QtWidgets.QListWidget(self.PFP_Tab_HEX)
        self.PFP_ListView_HEX.setObjectName("PFP_ListView_HEX")
        item = QtWidgets.QListWidgetItem()
        self.PFP_ListView_HEX.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.PFP_ListView_HEX.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.PFP_ListView_HEX.addItem(item)
        self.gridLayout_21.addWidget(self.PFP_ListView_HEX, 0, 0, 1, 1)
        self.PFP_TabView_PacketArea.addTab(self.PFP_Tab_HEX, "")
        self.gridLayout_9.addWidget(self.PFP_TabView_PacketArea, 1, 0, 2, 1)
        self.gridLayout_7.addWidget(self.PFP_Frame_PacketArea, 2, 0, 1, 2)
        self.PFP_Frame_FieldArea = QtWidgets.QFrame(self.PFP_GroupBox_PacketFromPCAPView)
        self.PFP_Frame_FieldArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PFP_Frame_FieldArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PFP_Frame_FieldArea.setObjectName("PFP_Frame_FieldArea")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.PFP_Frame_FieldArea)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.PFP_TableView_Field = QtWidgets.QTableWidget(self.PFP_Frame_FieldArea)
        self.PFP_TableView_Field.setObjectName("PFP_TableView_Field")
        self.PFP_TableView_Field.setColumnCount(4)
        self.PFP_TableView_Field.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.PFP_TableView_Field.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PFP_TableView_Field.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.PFP_TableView_Field.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.PFP_TableView_Field.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.PFP_TableView_Field.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.PFP_TableView_Field.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PFP_TableView_Field.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.PFP_TableView_Field.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.PFP_TableView_Field.setHorizontalHeaderItem(3, item)
        self.gridLayout_10.addWidget(self.PFP_TableView_Field, 1, 0, 1, 4)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem13, 3, 0, 1, 1)
        self.PFP_Button_ShowModification = QtWidgets.QPushButton(self.PFP_Frame_FieldArea)
        self.PFP_Button_ShowModification.setObjectName("PFP_Button_ShowModification")
        self.gridLayout_10.addWidget(self.PFP_Button_ShowModification, 3, 1, 1, 1)
        self.PFP_Button_Forward = QtWidgets.QPushButton(self.PFP_Frame_FieldArea)
        self.PFP_Button_Forward.setObjectName("PFP_Button_Forward")
        self.gridLayout_10.addWidget(self.PFP_Button_Forward, 3, 2, 1, 1)
        self.PFP_Button_Drop = QtWidgets.QPushButton(self.PFP_Frame_FieldArea)
        self.PFP_Button_Drop.setObjectName("PFP_Button_Drop")
        self.gridLayout_10.addWidget(self.PFP_Button_Drop, 3, 3, 1, 1)
        self.PFP_Label_FieldArea = QtWidgets.QLabel(self.PFP_Frame_FieldArea)
        self.PFP_Label_FieldArea.setObjectName("PFP_Label_FieldArea")
        self.gridLayout_10.addWidget(self.PFP_Label_FieldArea, 0, 0, 1, 4)
        self.PFP_Label_Information = QtWidgets.QLabel(self.PFP_Frame_FieldArea)
        self.PFP_Label_Information.setObjectName("PFP_Label_Information")
        self.gridLayout_10.addWidget(self.PFP_Label_Information, 2, 0, 1, 2)
        self.gridLayout_7.addWidget(self.PFP_Frame_FieldArea, 3, 0, 1, 1)
        self.PFP_Frame_PCAPFile = QtWidgets.QFrame(self.PFP_GroupBox_PacketFromPCAPView)
        self.PFP_Frame_PCAPFile.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PFP_Frame_PCAPFile.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PFP_Frame_PCAPFile.setObjectName("PFP_Frame_PCAPFile")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.PFP_Frame_PCAPFile)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.PFP_Label_PCAPFile_2 = QtWidgets.QLabel(self.PFP_Frame_PCAPFile)
        self.PFP_Label_PCAPFile_2.setObjectName("PFP_Label_PCAPFile_2")
        self.gridLayout_12.addWidget(self.PFP_Label_PCAPFile_2, 1, 0, 1, 1)
        self.PFP_Textbox_PCAPFilePath = QtWidgets.QLineEdit(self.PFP_Frame_PCAPFile)
        self.PFP_Textbox_PCAPFilePath.setText("")
        self.PFP_Textbox_PCAPFilePath.setAlignment(QtCore.Qt.AlignCenter)
        self.PFP_Textbox_PCAPFilePath.setObjectName("PFP_Textbox_PCAPFilePath")
        self.gridLayout_12.addWidget(self.PFP_Textbox_PCAPFilePath, 1, 1, 1, 1)
        self.PFP_Label_PCAPFile = QtWidgets.QLabel(self.PFP_Frame_PCAPFile)
        self.PFP_Label_PCAPFile.setObjectName("PFP_Label_PCAPFile")
        self.gridLayout_12.addWidget(self.PFP_Label_PCAPFile, 0, 0, 1, 4)
        self.PFP_Button_Open = QtWidgets.QPushButton(self.PFP_Frame_PCAPFile)
        self.PFP_Button_Open.setObjectName("PFP_Button_Open")
        self.gridLayout_12.addWidget(self.PFP_Button_Open, 1, 2, 1, 1)
        self.PFP_Button_Cancel = QtWidgets.QPushButton(self.PFP_Frame_PCAPFile)
        self.PFP_Button_Cancel.setObjectName("PFP_Button_Cancel")
        self.gridLayout_12.addWidget(self.PFP_Button_Cancel, 1, 3, 1, 1)
        self.gridLayout_7.addWidget(self.PFP_Frame_PCAPFile, 0, 0, 1, 2)
        self.gridLayout_11.addWidget(self.PFP_GroupBox_PacketFromPCAPView, 4, 0, 1, 1)
        self.StackView.addWidget(self.PacketFromPCAPView)
        self.gridLayout.addWidget(self.StackView, 0, 1, 1, 1)
        self.OptionView = QtWidgets.QFrame(self.centralwidget)
        self.OptionView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.OptionView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OptionView.setObjectName("OptionView")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.OptionView)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.OV_GroupBox = QtWidgets.QGroupBox(self.OptionView)
        self.OV_GroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.OV_GroupBox.setObjectName("OV_GroupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.OV_GroupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.OV_HookButton = QtWidgets.QPushButton(self.OV_GroupBox)
        self.OV_HookButton.setObjectName("OV_HookButton")
        self.verticalLayout_7.addWidget(self.OV_HookButton)
        self.OV_HookCollectionButton = QtWidgets.QPushButton(self.OV_GroupBox)
        self.OV_HookCollectionButton.setObjectName("OV_HookCollectionButton")
        self.verticalLayout_7.addWidget(self.OV_HookCollectionButton)
        self.OV_LivePacketButton = QtWidgets.QPushButton(self.OV_GroupBox)
        self.OV_LivePacketButton.setObjectName("OV_LivePacketButton")
        self.verticalLayout_7.addWidget(self.OV_LivePacketButton)
        self.OV_PacketFromPCAPButton = QtWidgets.QPushButton(self.OV_GroupBox)
        self.OV_PacketFromPCAPButton.setObjectName("OV_PacketFromPCAPButton")
        self.verticalLayout_7.addWidget(self.OV_PacketFromPCAPButton)
        spacerItem14 = QtWidgets.QSpacerItem(139, 527, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem14)
        self.verticalLayout_6.addWidget(self.OV_GroupBox)
        self.gridLayout.addWidget(self.OptionView, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1139, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.StackView.setCurrentIndex(0)
        self.LPV_TabView_PacketArea.setCurrentIndex(0)
        self.PFP_TabView_PacketArea.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ##Button logic##
        # For Hook view
        self.OV_HookButton.clicked.connect(lambda: self.setPage(self.StackView, 1))
        self.HV_TC_AddHookButton.clicked.connect(lambda: self.createHookDialog(CreateEditHook()))
        self.HV_TC_EditButton.clicked.connect(lambda: self.createEditDialog(CreateEditHook(),"edithook"))  # TODO Accept selected Hook to edit
        
        # For Hook Collection View
        self.OV_HookCollectionButton.clicked.connect(lambda: self.setPage(self.StackView, 2))
        self.Button_AddHookCollection.clicked.connect(lambda: self.createEditDialog(CreateEditHookCollection(),"addcoll"))
        self.Button_Edit.clicked.connect(lambda: self.createEditDialog(CreateEditHookCollection(),"editcoll")) # TODO Accept selected Hook collection to edit
        
        # For Live Packet View
        self.OV_LivePacketButton.clicked.connect(lambda: self.setPage(self.StackView, 3))
        self.LPV_ComboBox_ProxyBehavior.currentTextChanged.connect(lambda: self.isEnabled(self.LPV_ComboBox_ProxyBehavior, self.LPV_ComboBox_InterceptionBehavior, self.LPV_TextBox_QueueSize))
        self.LPV_ComboBox_InterceptionBehavior.currentTextChanged.connect(lambda: self.enableInterceptor(self.LPV_ComboBox_InterceptionBehavior))
        self.LPV_TextBox_QueueSize.textChanged.connect(lambda: self.setQueueSize(self.LPV_TextBox_QueueSize))
        
        # For PCAP View
        self.OV_PacketFromPCAPButton.clicked.connect(lambda: self.setPage(self.StackView, 4))

    #Get new Collection info
    def createEditDialog(self, dialogType,checkType):
        Dialog = QtWidgets.QDialog()
        hookDialog = dialogType
        hookDialog.setupUi(Dialog,manager)
        hookDialog.updateHookBox()
        Dialog.exec_()

        if hookDialog:
            if (checkType=="addcoll"):
                #get what the user put in
                name = hookDialog.nameBox.text()
                seq = hookDialog.seqBox.text()
                stat = hookDialog.statusBox.currentText()
                desc = hookDialog.descBox.text()
                
                #determine enabled/disabled status
                if(stat.lower()=="enabled"):
                    stat = True
                else:
                    stat = False
                if (name != "" and seq != ""): #only save if there's a name and sequence number there!
                    newColl = HookCollection(name,seq,stat,desc,[])
                    manager.addHookCollection(newColl)
                    self.updateCollectionGui(manager)
    
    #this is for creating new hooks using the Hook view
    def createHookDialog(self,dialogType):
        Dialog = QtWidgets.QDialog()
        hookDialog = dialogType
        hookDialog.setupUi(Dialog,self.manager) #we pass the manager to the dialog
        Dialog.exec_() #execture the dialog
        
        if hookDialog: #get the text from the add hook dialog
            name = hookDialog.TextBox_HookName.text()
            desc = hookDialog.TextBox_Description.text()
            path = hookDialog.TextBox_HookPath.text()

            newHook = Hook(name,False,desc,-1,path) #create hook
            manager.addHook(newHook) #add it to the system
            self.updateHookUI(manager) #update the UI to show the newly added hook



    def setPage(self, stackview, index):
        stackview.setCurrentIndex(index)

    def dialogWindow(self, title="", message=""):
        Dialog = QtWidgets.QDialog()
        okdialog = OkDialog()
        okdialog.setupUi(Dialog, title, message)
        Dialog.exec_()

    def isEnabled(self, combobox, interceptionButton, queueText):
        status = combobox.currentText()
        if(status == "Enabled"):
            self.dialogWindow("Proxy Behavior Enabled Notification",
                              "Proxy behavior has been enabled.\nThe system has backed up the system's proxy settings and will restore to it when the proxy behavior is disabled.")
            interceptionButton.setDisabled(False)
            queueText.setDisabled(False)
            #Proxy
            self.proxy = Proxy()
            self.proxyOn()
            #self.proxy.intercept()
            self.t1 = threading.Thread(target=self.proxy.intercept, args=(self.addPacket,))
            self.t1.setDaemon(True)
            self.t1.start()

        elif(status == "Disabled"):
            interceptionButton.setDisabled(True)
            queueText.setDisabled(True)
            self.dialogWindow("Proxy Behavior Disabled Notification",
                              "Proxy behavior has been disabled.\nThe system has restored to the previous proxy settings and it will stop appending packet information to the live traffic PCAP file.")
            self.proxyOff()

    def showHookInfo(self, hookProperties):
        hookProperties.show()

    def write(self, pkt):
        wrpcap(self.pcapName, pkt, append=True)

    def proxyOn(self):
        self.count = self.count+1
        self.pcapName = "live_traffic"+str(self.count)+".pcap"
        self.proxy.turnOn()

    def proxyOff(self):
        self.proxy.turnOff()

    def setCaptureFilter(self, capture):
        self.captureFilterExpression = capture.text()
        print(self.captureFilterExpression)

    def clearFilter(self):
        self.captureFilterExpression = ""


    def addPacket(self, packet):
        newPacker = packet
        if self.rulesP.captureFilterStatus:
            print("Passing by hooks!")
            hc = self.manager.getCollections()
            newPacker = self.manager.executeCollection(newPacker)
            #newPacker = sniff(filter=self.captureFilterExpression)

        pkt = Ether(newPacker.get_payload())/IP(newPacker.get_payload())
        self.write(pkt)
        ptype = pkt.sprintf("%.time% {TCP: TCP}{UDP: UDP}{ICMP:n ICMP} Packet")
        byt = bytes(pkt)
        
        item_0 = QtWidgets.QTreeWidgetItem(self.LPV_TreeView_Dissected, [ptype+" : "+pkt.summary()])
        #hexdump(pkt)
        #hexP = import_hexcap()
        
        #item = QtWidgets.QListWidgetItem()
        self.LPV_ListView_Binary.addItem(str(byt))
        self.LPV_ListView_HEX.addItem("Hex")
        #byteItem = QtWidgets.QListWidgetItem(self.PFP_ListView_Binary, ["Bytes"])
        
        for i in range(0,len(pkt[0])):
            print(i)
            child = QtWidgets.QTreeWidgetItem(item_0, [str(pkt[0][i].name)])
            for field, value in pkt.fields.items():
                child2 = QtWidgets.QTreeWidgetItem(child, [field+": "+str(value)])
        
        #print("HI!")

    def enableInterceptor(self, combobox):
        status = combobox.currentText()
        if(status == "Enabled"):
            self.rulesP.enableFilter()
        else:
            self.rulesP.disableFilter()

    def setQueueSize(self, text1):
        self.queue_size = text1.text()
        print(self.queue_size)

    #Build the UI to be contained in the Main window
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.HV_GroupBox_2.setTitle(_translate("MainWindow", "Content View"))
        self.HV_GroupBox.setTitle(_translate("MainWindow", "Hook View"))
        self.HV_TC_AddHookButton.setText(_translate("MainWindow", "+Hook"))
        self.HV_TC_EditButton.setText(_translate("MainWindow", "Edit"))
        self.HV_TC_DeleteButton.setText(_translate("MainWindow", "Delete"))
        self.HV_TC_SearchLabel.setText(_translate("MainWindow", "Search"))
        self.HV_TC_TextBox.setPlaceholderText(_translate("MainWindow", "Name of Hook"))
        self.HV_HookPropertiesGroupBox.setTitle(_translate("MainWindow", "Hook Properties"))
        self.HV_HP_HookTreeView.headerItem().setText(0, _translate("MainWindow", "Hook"))
        self.HV_HP_HookTreeView.headerItem().setText(1, _translate("MainWindow", "Description"))
        self.HV_HP_HookTreeView.headerItem().setText(2, _translate("MainWindow", "Association with Hook Collection"))
        __sortingEnabled = self.HV_HP_HookTreeView.isSortingEnabled()
        self.HV_HP_HookTreeView.setSortingEnabled(False)
        
        #Hook Collection Box
        self.GroupBox_HCV.setTitle(_translate("MainWindow", "Hook Collection View"))
        self.Button_AddHookCollection.setText(_translate("MainWindow", "+Hook Collection"))
        self.Button_Edit.setText(_translate("MainWindow", "Edit"))
        self.Button_Delete.setText(_translate("MainWindow", "Delete"))
        self.Label_Search.setText(_translate("MainWindow", "Search"))
        self.TextBox_Search.setPlaceholderText(_translate("MainWindow", "Name of Hook Collection"))
        self.HCV_HookCollectionProperties_GroupBox.setTitle(_translate("MainWindow", "Hook Collection Properties"))
        self.HCV_HCP_TreeView.headerItem().setText(0, _translate("MainWindow", "Hook Collection"))
        self.HCV_HCP_TreeView.headerItem().setText(1, _translate("MainWindow", "No. of Hooks"))
        self.HCV_HCP_TreeView.headerItem().setText(2, _translate("MainWindow", "Hook Collection Status"))
        self.HCV_HCP_TreeView.headerItem().setText(3, _translate("MainWindow", "Hook Collection Execution Sequence"))
        __sortingEnabled = self.HCV_HCP_TreeView.isSortingEnabled()
        self.HCV_HCP_TreeView.setSortingEnabled(False)

        #Packet Stuff
        self.LPV_GroupBox_LivePacketView.setTitle(_translate("MainWindow", "Live Packet View"))
        item = self.LPV_Table_FieldArea.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.LPV_Table_FieldArea.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.LPV_Table_FieldArea.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.LPV_Table_FieldArea.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.LPV_Table_FieldArea.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.LPV_Table_FieldArea.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Field Name"))
        item = self.LPV_Table_FieldArea.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        item = self.LPV_Table_FieldArea.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mask"))
        item = self.LPV_Table_FieldArea.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Display Format"))
        self.LPV_Button_ShowModification.setText(_translate("MainWindow", "Show Modification"))
        self.LPV_Button_Forward.setText(_translate("MainWindow", "Forward"))
        self.LPV_Button_Drop.setText(_translate("MainWindow", "Drop"))
        self.LPV_Label_FieldArea.setText(_translate("MainWindow", "Field Area"))
        self.LPV_Label_InformationalText.setText(_translate("MainWindow", "Field name, value and display format are editable fields."))
        self.LPV_TextBox_ReturnType.setPlaceholderText(_translate("MainWindow", "Return Type"))
        self.LPV_Label_FuzzingArea.setText(_translate("MainWindow", "Fuzzing Area"))
        self.LPV_Button_Stop.setText(_translate("MainWindow", "Stop"))
        self.LPV_Label_Minimum.setText(_translate("MainWindow", "Minimum"))
        self.LPV_Label_PacketName.setText(_translate("MainWindow", "Selected Packet Name"))
        self.LPV_Label_Maximum.setText(_translate("MainWindow", "Maximum"))
        self.LPV_Label_ReturnType.setText(_translate("MainWindow", "Expected Return Type"))
        self.LPV_TextBox_Maximum.setPlaceholderText(_translate("MainWindow", "Maximum"))
        self.LPV_TextBox_FieldName.setPlaceholderText(_translate("MainWindow", "Selected Field Name"))
        self.LPV_TextBox_PacketName.setPlaceholderText(_translate("MainWindow", "Selected Packet Name"))
        self.LPV_Button_Fuzz.setText(_translate("MainWindow", "Fuzz"))
        self.LPV_Label_FieldName.setText(_translate("MainWindow", "Selected Field Name"))
        self.LPV_TextBox_Minimum.setPlaceholderText(_translate("MainWindow", "Minimum"))
        self.LPV_Label_PacketArea.setText(_translate("MainWindow", "Packet Area"))
        self.LPV_Button_Clear_2.setText(_translate("MainWindow", "Clear"))
        self.LPV_Button_Clear.clicked.connect(lambda: self.clearFilter())
        self.LPV_TreeView_Dissected.headerItem().setText(0, _translate("MainWindow", ""))
        __sortingEnabled = self.LPV_TreeView_Dissected.isSortingEnabled()
        self.LPV_TreeView_Dissected.setSortingEnabled(False)
       # self.LPV_TreeView_Dissected.topLevelItem(0).setText(0, _translate("MainWindow", "New Item"))

        
        #self.LPV_TreeView_Dissected.topLevelItem(0).setText(0, _translate("MainWindow", "Packet"))
        
        self.LPV_TreeView_Dissected.setSortingEnabled(__sortingEnabled)
        self.LPV_TabView_PacketArea.setTabText(self.LPV_TabView_PacketArea.indexOf(self.LPV_Tab_Dissected), _translate("MainWindow", "Dissected"))
        __sortingEnabled = self.LPV_ListView_Binary.isSortingEnabled()
        self.LPV_ListView_Binary.setSortingEnabled(False)


        self.LPV_ListView_Binary.setSortingEnabled(__sortingEnabled)
        self.LPV_TabView_PacketArea.setTabText(self.LPV_TabView_PacketArea.indexOf(self.LPV_Tab_Binary), _translate("MainWindow", "Binary"))
        __sortingEnabled = self.LPV_ListView_HEX.isSortingEnabled()
        self.LPV_ListView_HEX.setSortingEnabled(False)
       
        #Fake packet items - these should be deleted after the gui supports the actual model of our system

        self.LPV_ListView_HEX.setSortingEnabled(__sortingEnabled)
        self.LPV_TabView_PacketArea.setTabText(self.LPV_TabView_PacketArea.indexOf(self.LPV_Tab_HEX), _translate("MainWindow", "HEX"))
        self.LPV_Label_Filter.setText(_translate("MainWindow", "Filter"))
        self.LPV_TextBox_FilterExpression.setPlaceholderText(_translate("MainWindow", "Filter Expression"))
        self.LPV_Label_CaptureFilter.setText(_translate("MainWindow", "Capture Filter"))
        self.LPV_Button_Apply.setText(_translate("MainWindow", "Apply"))
        self.LPV_Button_Clear.setText(_translate("MainWindow", "Clear"))
        self.LPV_Label_ProxyBehavior.setText(_translate("MainWindow", "Proxy Behavior"))
        self.LPV_ComboBox_ProxyBehavior.setItemText(0, _translate("MainWindow", "Disabled"))
        self.LPV_ComboBox_ProxyBehavior.setItemText(1, _translate("MainWindow", "Enabled"))
        self.LPV_Label_InterceptionBehavior.setText(_translate("MainWindow", "Interception Behavior"))
        self.LPV_ComboBox_InterceptionBehavior.setItemText(0, _translate("MainWindow", "Disabled"))
        self.LPV_ComboBox_InterceptionBehavior.setItemText(1, _translate("MainWindow", "Enabled"))
        self.LPV_Label_QueueSize.setText(_translate("MainWindow", "Queue Size"))
        self.LPV_TextBox_QueueSize.setPlaceholderText(_translate("MainWindow", "Queue Size"))
        self.PFP_GroupBox_PacketFromPCAPView.setTitle(_translate("MainWindow", "Packet from PCAP View"))
        self.PFP_Label_Filter.setText(_translate("MainWindow", "Filter"))
        self.PFP_TextBox_FilterExpression.setPlaceholderText(_translate("MainWindow", "Filter Expression"))
        self.PFP_Label_CaptureFilter.setText(_translate("MainWindow", "Capture Filter"))
        self.PFP_Button_Apply.setText(_translate("MainWindow", "Apply"))
        self.PFP_Button_Clear_2.setText(_translate("MainWindow", "Clear"))
        self.PFP_Textbox_ReturnType.setPlaceholderText(_translate("MainWindow", "Return Type"))
        self.PFP_Label_FuzzingArea.setText(_translate("MainWindow", "Fuzzing Area"))
        self.PFP_Button_Stop.setText(_translate("MainWindow", "Stop"))
        self.PFP_Label_Minimum.setText(_translate("MainWindow", "Minimum"))
        self.PFP_Label_SelectedPacketName.setText(_translate("MainWindow", "Selected Packet Name"))
        self.PFP_Label_Maximum.setText(_translate("MainWindow", "Maximum"))
        self.PFP_Label_ReturnType.setText(_translate("MainWindow", "Expected Return Type"))
        self.PFP_Textbox_Maximum.setPlaceholderText(_translate("MainWindow", "Maximum"))
        self.PFP_Textbox_FieldName.setPlaceholderText(_translate("MainWindow", "Selected Field Name"))
        self.PFP_Textbox_PacketName.setPlaceholderText(_translate("MainWindow", "Selected Packet Name"))
        self.PFP_Button_Fuzz.setText(_translate("MainWindow", "Fuzz"))
        self.PFP_Label_FieldName.setText(_translate("MainWindow", "Selected Field Name"))
        self.PFP_Textbox_Minimum.setPlaceholderText(_translate("MainWindow", "Minimum"))
        self.PFP_Label_PacketArea.setText(_translate("MainWindow", "Packet Area"))
        self.PFP_Button_Clear.setText(_translate("MainWindow", "Clear"))
        self.PFP_TreeView_Dissected.headerItem().setText(0, _translate("MainWindow", ""))
        __sortingEnabled = self.PFP_TreeView_Dissected.isSortingEnabled()
        self.PFP_TreeView_Dissected.setSortingEnabled(False)
        

        __sortingEnabled = self.PFP_ListView_Binary.isSortingEnabled()
        self.PFP_ListView_Binary.setSortingEnabled(False)

        
        
        self.PFP_TabView_PacketArea.setTabText(self.PFP_TabView_PacketArea.indexOf(self.PFP_Tab_Binary), _translate("MainWindow", "Binary"))
        __sortingEnabled = self.PFP_ListView_HEX.isSortingEnabled()
        self.PFP_ListView_HEX.setSortingEnabled(False)
        item = self.PFP_ListView_HEX.item(0)
        item.setText(_translate("MainWindow", "kasjdfsa jf;lsafjldaskf "))
        item = self.PFP_ListView_HEX.item(1)
        item.setText(_translate("MainWindow", "jskfadslkjfdsfda sfdsssssf "))
        item = self.PFP_ListView_HEX.item(2)
        item.setText(_translate("MainWindow", "ajsdfas jkfsjkfdasfadskdfjds"))
        self.PFP_ListView_HEX.setSortingEnabled(__sortingEnabled)
        self.PFP_TabView_PacketArea.setTabText(self.PFP_TabView_PacketArea.indexOf(self.PFP_Tab_HEX), _translate("MainWindow", "HEX"))
        item = self.PFP_TableView_Field.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.PFP_TableView_Field.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.PFP_TableView_Field.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.PFP_TableView_Field.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.PFP_TableView_Field.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.PFP_TableView_Field.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Field Name"))
        item = self.PFP_TableView_Field.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        item = self.PFP_TableView_Field.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mask"))
        item = self.PFP_TableView_Field.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Display Format"))
        self.PFP_Button_ShowModification.setText(_translate("MainWindow", "Show Modification"))
        self.PFP_Button_Forward.setText(_translate("MainWindow", "Forward"))
        self.PFP_Button_Drop.setText(_translate("MainWindow", "Drop"))
        self.PFP_Label_FieldArea.setText(_translate("MainWindow", "Field Area"))
        self.PFP_Label_Information.setText(_translate("MainWindow", "Field name, value and display format are editable fields."))
        self.PFP_Label_PCAPFile_2.setText(_translate("MainWindow", "PCAP File"))
        self.PFP_Textbox_PCAPFilePath.setPlaceholderText(_translate("MainWindow", "PCAP File Path"))
        self.PFP_Label_PCAPFile.setText(_translate("MainWindow", "PCAP File"))
        self.PFP_Button_Open.setText(_translate("MainWindow", "Open"))
        self.PFP_Button_Cancel.setText(_translate("MainWindow", "Cancel"))
        self.OV_GroupBox.setTitle(_translate("MainWindow", "Option View"))
        self.OV_HookButton.setText(_translate("MainWindow", "Hook"))
        self.OV_HookCollectionButton.setText(_translate("MainWindow", "Hook Collection"))
        self.OV_LivePacketButton.setText(_translate("MainWindow", "Live Packet"))
        self.OV_PacketFromPCAPButton.setText(_translate("MainWindow", "Packet from PCAP"))
    
    ###UPDATERS: These methods update the main GUI to reflect the model###
    
    ##FOR HOOK COLLECTION VIEW

     #Update the Hook Collection View GUI to show the Hook Collections (the top box in the Hook Collection View)
     #You should call this every time you add, delete, or edit a hook


    def updateCollectionGui(self,manager):
        self.HCV_HCP_TreeView.clear() #Dump everything currently displyed in the ui element! We're rebuilding it

        rowNum = 0 #current item being generated in the list

        for c in manager.collection: #for each hook collection in the manager, generate a new QTreeView item for it
            item_0 = QtWidgets.QTreeWidgetItem(self.HCV_HCP_TreeView)
            item_0.setCheckState(0, QtCore.Qt.Unchecked)

            self.HCV_HCP_TreeView.topLevelItem(rowNum).setText(0, c.getCollName()) #display Collection name
            self.HCV_HCP_TreeView.topLevelItem(rowNum).setText(1, str(len(c.getHooks()))) #display # of hooks the collection has
            self.HCV_HCP_TreeView.topLevelItem(rowNum).setText(2, str(c.getCollStatus())) #display the status of the Collection
            self.HCV_HCP_TreeView.topLevelItem(rowNum).setText(3, str(c.getCollSeqNum())) #display collection sequence number
            
            #Structure and display for Hook Collection description
            header = QtWidgets.QTreeWidgetItem(item_0)
            header.setText(0, "| Description |")
            child1 = QtWidgets.QTreeWidgetItem(item_0)
            child1.setText(0, c.getCollDesc())

            #Header and display of Hooks in the collection
            hookHeader = QtWidgets.QTreeWidgetItem(item_0)
            hook = QtWidgets.QTreeWidgetItem(item_0)
            hookHeader.setText(0,"| Hook |")
            hookHeader.setText(1, "| Description |")
            hookHeader.setText(2, "| Hook Status |")
            hookHeader.setText(3, "| Hook Execution Sequence |")

            for h in c.getHooks(): #for each hook, get its info and display it

                hook.setText(0, h.getName())
                hook.setText(1, h.getDesc())
                hook.setText(2, str(h.getStatus()))
                hook.setText(3, str(h.getSeqNum()))

            rowNum+=1 #makes sure we're placing each new hook collection in a new row
        return

    ##HOOK VIEW UPDATER
    def updateHookUI(self,manager):
        self.HV_HP_HookTreeView.clear() #Dump everything currently displyed in the ui element! We're rebuilding it

        rowNum = 0 #current item being generated in the list

        for h in manager.hooks: #for each hook in the manager, generate a new QTreeView item for it
            item_0 = QtWidgets.QTreeWidgetItem(self.HV_HP_HookTreeView)
            item_0.setCheckState(0, QtCore.Qt.Unchecked)

            self.HV_HP_HookTreeView.topLevelItem(rowNum).setText(0, h.getName()) #display hook name
            self.HV_HP_HookTreeView.topLevelItem(rowNum).setText(1, h.getDesc()) #display hook description
            self.HV_HP_HookTreeView.topLevelItem(rowNum).setText(2, str(h.getAssocNum())) #display the # of associations

            rowNum+=1   

        return

    ##END HOOK VIEW UPDATER

    ##FOR LIVE PACKET
        #TODO: add updaters for the Packet view here

    ##END LIVE PACKET VIEW UPDATERS

    ##FOR PCAP
        #TODO: add updaters for the PCAP view here

    ##END PCAP VIEW UPDATERS
        
###end of UI class###

#test the UI's ability to represent our model by creating a manager with 4 collections in it
    def buildSample():
        #create a hook called 'testHook'with the name 'Test'. Its sequence is not set automatically.
        testHook = Hook("Test1",True,"A test hook!",0,"C:/Users/octob/Documents/NTPSProject/Interceptor/testHook.py")
        testHook1 = Hook("Test2",True,"A test hook!",0,"C:/Users/octob/Documents/NTPSProject/Interceptor/testHook.py")
        testHook2 = Hook("Test3",True,"A test hook!",0,"C:/Users/octob/Documents/NTPSProject/Interceptor/testHook.py")
        testHook3 = Hook("Test4",True,"A test hook!",0,"C:/Users/octob/Documents/NTPSProject/Interceptor/testHook.py")

        #create hook collections and put the hooks list in it
        hc = HookCollection("testColl1",0,True,"A test hook collection.",[testHook])
        hc1 = HookCollection("testColl2",1,True,"A test hook collection.",[testHook1])
        hc2 = HookCollection("testColl3",2,True,"A test hook collection.",[testHook2])
        hc3 = HookCollection("testColl4",3,True,"A test hook collection.",[testHook3])

        #create a list of HookCollections; right now, there's only one hook collection in it
        collections = [hc]
        collections.append(hc1)
        collections.append(hc2)
        collections.append(hc3)

        #create HookCollectionManager called 'manager' and add 'collections' to it.
        #remember that managers also store hooks without assigning them to collections; 
        #we add a copy of the testHook to illustrate this.
        self.manager = HookCollectionManager(collections,[])

        return self.manager


#we actually generate the application we see when we run the python file here
if __name__ == "__main__":
    #Imports need to be done forthis main method for the classes to work
    import sys

    app = QtWidgets.QApplication(sys.argv) #create new instance of the application
    MainWindow = QtWidgets.QMainWindow() #Create a new main window
    ui = Ui_MainWindow() #create a ui
    ui.setupUi(MainWindow) #attach the generated ui to the main window 

    manager = HookCollectionManager([],[]) #generate a fake set of collections to test the display
    ui.manager = manager

    #ui.updateCollectionGui(manager) #update the ui to display the collections
    #ui.updateCollectionHookList(manager.getCollections()[0]) #right now, we only display the hooks of the first collection

    MainWindow.show() #display the main window
    import atexit
    @atexit.register
    def reset():
        ui.rulesP.flush()
    sys.exit(app.exec_())
