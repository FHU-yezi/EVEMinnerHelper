# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EVE ��������AmuTSA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import (QCheckBox, QComboBox, QDoubleSpinBox, QFormLayout,
                             QGridLayout, QGroupBox, QHBoxLayout, QLabel,
                             QPushButton, QRadioButton, QSizePolicy,
                             QSpacerItem, QSpinBox, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(704, 538)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(704, 538))
        MainWindow.setMaximumSize(QSize(704, 538))
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.groupBox = QGroupBox(MainWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 50, 191, 161))
        self.formLayoutWidget = QWidget(self.groupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 160, 81))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.OreType = QComboBox(self.formLayoutWidget)
        self.OreType.setObjectName(u"OreType")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.OreType)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.OreVolume = QDoubleSpinBox(self.formLayoutWidget)
        self.OreVolume.setObjectName(u"OreVolume")
        self.OreVolume.setMaximum(50.000000000000000)
        self.OreVolume.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.OreVolume)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.OrePrice = QSpinBox(self.formLayoutWidget)
        self.OrePrice.setObjectName(u"OrePrice")
        self.OrePrice.setMaximum(10000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.OrePrice)

        self.OreDataSettings = QPushButton(self.groupBox)
        self.OreDataSettings.setObjectName(u"OreDataSettings")
        self.OreDataSettings.setGeometry(QRect(30, 110, 121, 31))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(13)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.OreDataSettings.setFont(font1)
        self.groupBox_2 = QGroupBox(MainWindow)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(220, 20, 201, 81))
        self.formLayoutWidget_2 = QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 20, 181, 51))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.ShipCapacity = QSpinBox(self.formLayoutWidget_2)
        self.ShipCapacity.setObjectName(u"ShipCapacity")
        self.ShipCapacity.setMaximum(10000000)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.ShipCapacity)

        self.ShipPrice = QSpinBox(self.formLayoutWidget_2)
        self.ShipPrice.setObjectName(u"ShipPrice")
        self.ShipPrice.setMaximum(1000000000)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.ShipPrice)

        self.groupBox_3 = QGroupBox(MainWindow)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(210, 100, 211, 111))
        self.verticalLayoutWidget = QWidget(self.groupBox_3)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 191, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.EnableCrashRisk = QCheckBox(self.verticalLayoutWidget)
        self.EnableCrashRisk.setObjectName(u"EnableCrashRisk")
        self.EnableCrashRisk.setAutoFillBackground(False)
        self.EnableCrashRisk.setChecked(True)

        self.verticalLayout.addWidget(self.EnableCrashRisk)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.CrashOreLostProportion = QDoubleSpinBox(self.verticalLayoutWidget)
        self.CrashOreLostProportion.setObjectName(u"CrashOreLostProportion")
        self.CrashOreLostProportion.setMaximum(1.000000000000000)
        self.CrashOreLostProportion.setSingleStep(0.010000000000000)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.CrashOreLostProportion)

        self.CrashProbability = QDoubleSpinBox(self.verticalLayoutWidget)
        self.CrashProbability.setObjectName(u"CrashProbability")
        self.CrashProbability.setMaximum(1.000000000000000)
        self.CrashProbability.setSingleStep(0.010000000000000)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.CrashProbability)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.groupBox_4 = QGroupBox(MainWindow)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(430, 20, 261, 191))
        self.formLayoutWidget_4 = QWidget(self.groupBox_4)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(10, 20, 241, 91))
        self.formLayout_4 = QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.formLayoutWidget_4)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.MiningVolumePerMachine = QDoubleSpinBox(self.formLayoutWidget_4)
        self.MiningVolumePerMachine.setObjectName(u"MiningVolumePerMachine")
        self.MiningVolumePerMachine.setMaximum(100000.000000000000000)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.MiningVolumePerMachine)

        self.label_13 = QLabel(self.formLayoutWidget_4)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.MiningMachineCount = QSpinBox(self.formLayoutWidget_4)
        self.MiningMachineCount.setObjectName(u"MiningMachineCount")
        self.MiningMachineCount.setMaximum(10)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.MiningMachineCount)

        self.label_15 = QLabel(self.formLayoutWidget_4)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_15)

        self.TimePerMachineMining = QSpinBox(self.formLayoutWidget_4)
        self.TimePerMachineMining.setObjectName(u"TimePerMachineMining")
        self.TimePerMachineMining.setMaximum(600)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.TimePerMachineMining)

        self.formLayoutWidget_7 = QWidget(self.groupBox_4)
        self.formLayoutWidget_7.setObjectName(u"formLayoutWidget_7")
        self.formLayoutWidget_7.setGeometry(QRect(10, 120, 241, 61))
        self.formLayout_8 = QFormLayout(self.formLayoutWidget_7)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.formLayoutWidget_7)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.MiningAdditionProportion = QDoubleSpinBox(self.formLayoutWidget_7)
        self.MiningAdditionProportion.setObjectName(u"MiningAdditionProportion")
        self.MiningAdditionProportion.setMaximum(1.000000000000000)
        self.MiningAdditionProportion.setSingleStep(0.010000000000000)

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.MiningAdditionProportion)

        self.label_16 = QLabel(self.formLayoutWidget_7)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_16)

        self.TimeProportionPerMining = QDoubleSpinBox(self.formLayoutWidget_7)
        self.TimeProportionPerMining.setObjectName(u"TimeProportionPerMining")
        self.TimeProportionPerMining.setMaximum(0.990000000000000)
        self.TimeProportionPerMining.setSingleStep(0.010000000000000)

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.TimeProportionPerMining)

        self.groupBox_6 = QGroupBox(MainWindow)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(20, 360, 671, 121))
        self.gridLayoutWidget = QWidget(self.groupBox_6)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 20, 191, 91))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.TimePerMining = QLabel(self.gridLayoutWidget)
        self.TimePerMining.setObjectName(u"TimePerMining")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.TimePerMining.setFont(font2)
        self.TimePerMining.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.TimePerMining, 0, 1, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 1, 0, 1, 1)

        self.TimePerCycle = QLabel(self.gridLayoutWidget)
        self.TimePerCycle.setObjectName(u"TimePerCycle")
        self.TimePerCycle.setFont(font2)
        self.TimePerCycle.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.TimePerCycle, 1, 1, 1, 1)

        self.CyclesCountPerHour = QLabel(self.gridLayoutWidget)
        self.CyclesCountPerHour.setObjectName(u"CyclesCountPerHour")
        self.CyclesCountPerHour.setFont(font2)
        self.CyclesCountPerHour.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.CyclesCountPerHour, 2, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 2, 0, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.groupBox_6)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(220, 20, 201, 91))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MiningCountPerHour = QLabel(self.gridLayoutWidget_2)
        self.MiningCountPerHour.setObjectName(u"MiningCountPerHour")
        self.MiningCountPerHour.setFont(font2)
        self.MiningCountPerHour.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.MiningCountPerHour, 2, 1, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget_2)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_2.addWidget(self.label_23, 0, 0, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget_2)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_2.addWidget(self.label_25, 2, 0, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_2)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_2.addWidget(self.label_26, 1, 0, 1, 1)

        self.MiningCountPerCycle = QLabel(self.gridLayoutWidget_2)
        self.MiningCountPerCycle.setObjectName(u"MiningCountPerCycle")
        self.MiningCountPerCycle.setFont(font2)
        self.MiningCountPerCycle.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.MiningCountPerCycle, 0, 1, 1, 1)

        self.MiningCountPerSecond = QLabel(self.gridLayoutWidget_2)
        self.MiningCountPerSecond.setObjectName(u"MiningCountPerSecond")
        self.MiningCountPerSecond.setFont(font2)
        self.MiningCountPerSecond.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.MiningCountPerSecond, 1, 1, 1, 1)

        self.gridLayoutWidget_3 = QWidget(self.groupBox_6)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(430, 20, 231, 91))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.RealProfitPerHour = QLabel(self.gridLayoutWidget_3)
        self.RealProfitPerHour.setObjectName(u"RealProfitPerHour")
        self.RealProfitPerHour.setFont(font2)
        self.RealProfitPerHour.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.RealProfitPerHour, 2, 1, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_3)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_3.addWidget(self.label_27, 0, 0, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget_3)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_3.addWidget(self.label_31, 2, 0, 1, 1)

        self.ProfitPerHourTheoretical = QLabel(self.gridLayoutWidget_3)
        self.ProfitPerHourTheoretical.setObjectName(u"ProfitPerHourTheoretical")
        self.ProfitPerHourTheoretical.setFont(font2)
        self.ProfitPerHourTheoretical.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.ProfitPerHourTheoretical, 0, 1, 1, 1)

        self.label_30 = QLabel(self.gridLayoutWidget_3)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_3.addWidget(self.label_30, 1, 0, 1, 1)

        self.CrashRiskToMoney = QLabel(self.gridLayoutWidget_3)
        self.CrashRiskToMoney.setObjectName(u"CrashRiskToMoney")
        self.CrashRiskToMoney.setFont(font2)
        self.CrashRiskToMoney.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.CrashRiskToMoney, 1, 1, 1, 1)

        self.groupBox_5 = QGroupBox(MainWindow)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(20, 220, 671, 131))
        self.gridLayoutWidget_4 = QWidget(self.groupBox_5)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 20, 651, 101))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_21 = QLabel(self.gridLayoutWidget_4)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_21)

        self.TimeToSaveOrePoint = QDoubleSpinBox(self.gridLayoutWidget_4)
        self.TimeToSaveOrePoint.setObjectName(u"TimeToSaveOrePoint")
        self.TimeToSaveOrePoint.setMaximum(180.000000000000000)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.TimeToSaveOrePoint)

        self.label_22 = QLabel(self.gridLayoutWidget_4)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_22)

        self.TimeOfSaveOre = QDoubleSpinBox(self.gridLayoutWidget_4)
        self.TimeOfSaveOre.setObjectName(u"TimeOfSaveOre")
        self.TimeOfSaveOre.setMaximum(60.000000000000000)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.TimeOfSaveOre)


        self.gridLayout_4.addLayout(self.formLayout_5, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_33 = QLabel(self.gridLayoutWidget_4)
        self.label_33.setObjectName(u"label_33")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_33)

        self.label_34 = QLabel(self.gridLayoutWidget_4)
        self.label_34.setObjectName(u"label_34")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_34)

        self.label_35 = QLabel(self.gridLayoutWidget_4)
        self.label_35.setObjectName(u"label_35")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_35)

        self.CongestionIndex = QDoubleSpinBox(self.gridLayoutWidget_4)
        self.CongestionIndex.setObjectName(u"CongestionIndex")
        self.CongestionIndex.setDecimals(1)
        self.CongestionIndex.setMaximum(30.000000000000000)
        self.CongestionIndex.setSingleStep(0.100000000000000)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.CongestionIndex)

        self.TimeOfSellOre = QDoubleSpinBox(self.gridLayoutWidget_4)
        self.TimeOfSellOre.setObjectName(u"TimeOfSellOre")
        self.TimeOfSellOre.setMaximum(60.000000000000000)

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.TimeOfSellOre)

        self.TimeToSellOrePoint = QDoubleSpinBox(self.gridLayoutWidget_4)
        self.TimeToSellOrePoint.setObjectName(u"TimeToSellOrePoint")
        self.TimeToSellOrePoint.setMaximum(180.000000000000000)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.TimeToSellOrePoint)


        self.gridLayout_4.addLayout(self.formLayout_6, 1, 4, 1, 1)

        self.SellOreWhenFull = QRadioButton(self.gridLayoutWidget_4)
        self.SellOreWhenFull.setObjectName(u"SellOreWhenFull")

        self.gridLayout_4.addWidget(self.SellOreWhenFull, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.SaveOreWhenFull = QRadioButton(self.gridLayoutWidget_4)
        self.SaveOreWhenFull.setObjectName(u"SaveOreWhenFull")

        self.gridLayout_4.addWidget(self.SaveOreWhenFull, 0, 2, 1, 1)

        self.DropOreWhenFull = QRadioButton(self.gridLayoutWidget_4)
        self.DropOreWhenFull.setObjectName(u"DropOreWhenFull")

        self.gridLayout_4.addWidget(self.DropOreWhenFull, 0, 0, 1, 1)

        self.label_36 = QLabel(MainWindow)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(20, 10, 131, 16))
        self.label_37 = QLabel(MainWindow)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(20, 30, 54, 12))
        self.Version = QLabel(MainWindow)
        self.Version.setObjectName(u"Version")
        self.Version.setGeometry(QRect(80, 30, 70, 12))
        self.horizontalLayoutWidget = QWidget(MainWindow)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 490, 671, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.CopyResult = QPushButton(self.horizontalLayoutWidget)
        self.CopyResult.setObjectName(u"CopyResult")
        self.CopyResult.setEnabled(True)
        self.CopyResult.setFont(font1)

        self.horizontalLayout.addWidget(self.CopyResult)

        self.horizontalSpacer_3 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.Compute = QPushButton(self.horizontalLayoutWidget)
        self.Compute.setObjectName(u"Compute")
        self.Compute.setFont(font1)

        self.horizontalLayout.addWidget(self.Compute)

        self.horizontalSpacer_4 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.ClearAll = QPushButton(self.horizontalLayoutWidget)
        self.ClearAll.setObjectName(u"ClearAll")
        self.ClearAll.setFont(font1)

        self.horizontalLayout.addWidget(self.ClearAll)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        QWidget.setTabOrder(self.OreType, self.OreVolume)
        QWidget.setTabOrder(self.OreVolume, self.OrePrice)
        QWidget.setTabOrder(self.OrePrice, self.ShipPrice)
        QWidget.setTabOrder(self.ShipPrice, self.ShipCapacity)
        QWidget.setTabOrder(self.ShipCapacity, self.EnableCrashRisk)
        QWidget.setTabOrder(self.EnableCrashRisk, self.CrashProbability)
        QWidget.setTabOrder(self.CrashProbability, self.CrashOreLostProportion)
        QWidget.setTabOrder(self.CrashOreLostProportion, self.MiningVolumePerMachine)
        QWidget.setTabOrder(self.MiningVolumePerMachine, self.MiningMachineCount)
        QWidget.setTabOrder(self.MiningMachineCount, self.TimePerMachineMining)
        QWidget.setTabOrder(self.TimePerMachineMining, self.MiningAdditionProportion)
        QWidget.setTabOrder(self.MiningAdditionProportion, self.TimeProportionPerMining)
        QWidget.setTabOrder(self.TimeProportionPerMining, self.DropOreWhenFull)
        QWidget.setTabOrder(self.DropOreWhenFull, self.SaveOreWhenFull)
        QWidget.setTabOrder(self.SaveOreWhenFull, self.SellOreWhenFull)
        QWidget.setTabOrder(self.SellOreWhenFull, self.TimeToSaveOrePoint)
        QWidget.setTabOrder(self.TimeToSaveOrePoint, self.TimeOfSaveOre)
        QWidget.setTabOrder(self.TimeOfSaveOre, self.TimeToSellOrePoint)
        QWidget.setTabOrder(self.TimeToSellOrePoint, self.CongestionIndex)
        QWidget.setTabOrder(self.CongestionIndex, self.TimeOfSellOre)
        QWidget.setTabOrder(self.TimeOfSellOre, self.Compute)
        QWidget.setTabOrder(self.Compute, self.CopyResult)
        QWidget.setTabOrder(self.CopyResult, self.ClearAll)
        QWidget.setTabOrder(self.ClearAll, self.OreDataSettings)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EVE \u77ff\u5de5\u52a9\u624b", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u77ff\u77f3\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u77ff\u77f3\u79cd\u7c7b", None))
#if QT_CONFIG(tooltip)
        self.OreType.setToolTip(QCoreApplication.translate("MainWindow", u"\u8981\u91c7\u96c6\u7684\u77ff\u77f3\u79cd\u7c7b", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4e2a\u4f53\u79ef", None))
#if QT_CONFIG(tooltip)
        self.OreVolume.setToolTip(QCoreApplication.translate("MainWindow", u"\u5355\u4e2a\u8be5\u79cd\u77ff\u77f3\u7684\u4f53\u79ef", None))
#endif // QT_CONFIG(tooltip)
        self.OreVolume.setSuffix(QCoreApplication.translate("MainWindow", u" m\u00b3", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4e2a\u4ef7\u503c", None))
#if QT_CONFIG(tooltip)
        self.OrePrice.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u5355\u4e2a\u8be5\u79cd\u77ff\u77f3\u7684\u4ef7\u683c</p><p>\u5efa\u8bae\u9009\u62e9\u5e02\u573a\u4e2d\u8f83\u4e3a\u666e\u904d\u7684\u62a5\u4ef7</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.OrePrice.setSuffix(QCoreApplication.translate("MainWindow", u" ISK", None))
        self.OrePrice.setPrefix("")
#if QT_CONFIG(tooltip)
        self.OreDataSettings.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bf9\u4e0d\u540c\u77ff\u77f3\u7684\u9ed8\u8ba4\u4ef7\u683c\u8fdb\u884c\u8c03\u6574", None))
#endif // QT_CONFIG(tooltip)
        self.OreDataSettings.setText(QCoreApplication.translate("MainWindow", u"\u77ff\u77f3\u6570\u636e\u8bbe\u7f6e", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8230\u8239\u8bbe\u7f6e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8230\u8239\u4ef7\u503c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u77ff\u77f3\u5bb9\u91cf", None))
#if QT_CONFIG(tooltip)
        self.ShipCapacity.setToolTip(QCoreApplication.translate("MainWindow", u"\u8230\u8239\u77ff\u77f3\u4ed3\u7684\u5bb9\u91cf", None))
#endif // QT_CONFIG(tooltip)
        self.ShipCapacity.setSuffix(QCoreApplication.translate("MainWindow", u" m\u00b3", None))
#if QT_CONFIG(tooltip)
        self.ShipPrice.setToolTip(QCoreApplication.translate("MainWindow", u"\u91c7\u77ff\u8230\u8239\u7684\u4ef7\u503c\uff0c\u5305\u62ec\u88c5\u5907", None))
#endif // QT_CONFIG(tooltip)
        self.ShipPrice.setSuffix(QCoreApplication.translate("MainWindow", u" ISK", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u7206\u8239\u6298\u503c\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.EnableCrashRisk.setToolTip(QCoreApplication.translate("MainWindow", u"\u8be5\u529f\u80fd\u5c06\u4f1a\u6839\u636e\u7206\u8239\u7684\u6982\u7387\uff0c\u5c06\u635f\u5931\u6298\u7b97\u5230\u6bcf\u6b21\u6316\u77ff\u6d41\u7a0b\u4e2d", None))
#endif // QT_CONFIG(tooltip)
        self.EnableCrashRisk.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u7206\u8239\u6298\u503c\u8ba1\u7b97", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u7206\u8239\u7387", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u77ff\u7269\u635f\u5931\u7387", None))
#if QT_CONFIG(tooltip)
        self.CrashOreLostProportion.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u7206\u8239\u65f6\u77ff\u7269\u7684\u635f\u5931\u6bd4\u4f8b\uff0c\u4ecb\u4e8e 0 \u548c 1 \u4e4b\u95f4</p><p>\u5982\u7206\u8239\u65f6\u4f1a\u635f\u5931\u76f8\u5f53\u4e8e\u77ff\u4ed3\u5bb9\u91cf 30% \u7684\u77ff\u77f3\u5219\u586b\u5165 0.3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.CrashProbability.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4ecb\u4e8e 0 \u5230 1 \u4e4b\u95f4\u7684\u6570\u503c</p><p>\u5982 20% \u7206\u8239\u6982\u7387\u5219\u586b\u5165 0.2</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u91c7\u77ff\u5668\u8bbe\u7f6e", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u5355\u91c7\u77ff\u5668\u5355\u6b21\u5f00\u91c7\u91cf", None))
#if QT_CONFIG(tooltip)
        self.MiningVolumePerMachine.setToolTip(QCoreApplication.translate("MainWindow", u"\u6bcf\u4e2a\u91c7\u77ff\u5668\u6bcf\u6b21\u5faa\u73af\u7684\u5f00\u91c7\u91cf\uff0c\u4e0d\u5305\u542b\u6280\u80fd\u548c\u6539\u88c5\u52a0\u6210", None))
#endif // QT_CONFIG(tooltip)
        self.MiningVolumePerMachine.setSuffix(QCoreApplication.translate("MainWindow", u" m\u00b3", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u77ff\u5668\u6570\u91cf", None))
#if QT_CONFIG(tooltip)
        self.MiningMachineCount.setToolTip(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u7684\u91c7\u77ff\u5668\u603b\u6570", None))
#endif // QT_CONFIG(tooltip)
        self.MiningMachineCount.setSuffix(QCoreApplication.translate("MainWindow", u" \u4e2a", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u5355\u6b21\u5faa\u73af\u65f6\u95f4", None))
#if QT_CONFIG(tooltip)
        self.TimePerMachineMining.setToolTip(QCoreApplication.translate("MainWindow", u"\u91c7\u77ff\u5668\u5355\u6b21\u5faa\u73af\u7684\u65f6\u95f4\uff0c\u4e0d\u5305\u542b\u6280\u80fd\u548c\u6539\u88c5\u52a0\u6210", None))
#endif // QT_CONFIG(tooltip)
        self.TimePerMachineMining.setSuffix(QCoreApplication.translate("MainWindow", u" \u79d2", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u91c7\u91cf\u52a0\u6210\u6bd4\u4f8b    ", None))
#if QT_CONFIG(tooltip)
        self.MiningAdditionProportion.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6280\u80fd\u6216\u6539\u88c5\u5e26\u6765\u7684\u5355\u6b21\u5faa\u73af\u91c7\u77ff\u91cf\u52a0\u6210\uff0c\u4ecb\u4e8e 0 \u5230 1 \u4e4b\u95f4</p><p>\u5982\u6709 20% \u7684\u91c7\u77ff\u91cf\u52a0\u6210\uff0c\u5219\u586b\u5165 0.2</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u5faa\u73af\u52a0\u901f\u6bd4\u4f8b", None))
#if QT_CONFIG(tooltip)
        self.TimeProportionPerMining.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6280\u80fd\u6216\u6539\u88c5\u5e26\u6765\u7684\u5355\u6b21\u5faa\u73af\u65f6\u95f4\u51cf\u5c11\u52a0\u6210\uff0c\u4ecb\u4e8e 0 \u5230 1 \u4e4b\u95f4</p><p>\u5982\u5355\u6b21\u5faa\u73af\u65f6\u95f4\u7f29\u77ed 20%\uff0c\u5219\u586b\u5165 0.2</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97\u7ed3\u679c", None))
#if QT_CONFIG(tooltip)
        self.TimePerMining.setToolTip(QCoreApplication.translate("MainWindow", u"\u4ece\u77ff\u4ed3\u5168\u7a7a\u5230\u5168\u6ee1\uff0c\u8fdb\u884c\u91c7\u77ff\u4f5c\u4e1a\u7684\u65f6\u95f4\uff0c\u4e0d\u5305\u542b\u8def\u7a0b\u8017\u65f6", None))
#endif // QT_CONFIG(tooltip)
        self.TimePerMining.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u5355\u6b21\u5faa\u73af\u65f6\u95f4", None))
#if QT_CONFIG(tooltip)
        self.TimePerCycle.setToolTip(QCoreApplication.translate("MainWindow", u"\u4ece\u77ff\u4ed3\u5168\u7a7a\u5230\u5168\u6ee1\u7684\u8017\u65f6\uff0c\u5305\u542b\u4e3a\u5904\u7406\u77ff\u77f3\u8017\u8d39\u7684\u65f6\u95f4", None))
#endif // QT_CONFIG(tooltip)
        self.TimePerCycle.setText("")
#if QT_CONFIG(tooltip)
        self.CyclesCountPerHour.setToolTip(QCoreApplication.translate("MainWindow", u"\u6bcf\u5c0f\u65f6\u53ef\u4ee5\u91c7\u96c6\u7684\u77ff\u77f3\u4ed3\u6570", None))
#endif // QT_CONFIG(tooltip)
        self.CyclesCountPerHour.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5355\u6b21\u5f00\u91c7\u65f6\u95f4", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u6bcf\u5c0f\u65f6\u5faa\u73af\u6b21\u6570", None))
#if QT_CONFIG(tooltip)
        self.MiningCountPerHour.setToolTip(QCoreApplication.translate("MainWindow", u"\u5305\u542b\u8def\u7a0b\u65f6\u95f4\uff0c\u6298\u7b97\u6bcf\u5c0f\u65f6\u91c7\u96c6\u5230\u7684\u77ff\u77f3\u91cf", None))
#endif // QT_CONFIG(tooltip)
        self.MiningCountPerHour.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u5355\u6b21\u5faa\u73af\u5f00\u91c7\u91cf", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u6bcf\u5c0f\u65f6\u5f00\u91c7\u91cf", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u6bcf\u79d2\u5f00\u91c7\u91cf", None))
#if QT_CONFIG(tooltip)
        self.MiningCountPerCycle.setToolTip(QCoreApplication.translate("MainWindow", u"\u6bcf\u77ff\u4ed3\u6240\u80fd\u5bb9\u7eb3\u7684\u77ff\u77f3\u603b\u6570", None))
#endif // QT_CONFIG(tooltip)
        self.MiningCountPerCycle.setText("")
#if QT_CONFIG(tooltip)
        self.MiningCountPerSecond.setToolTip(QCoreApplication.translate("MainWindow", u"\u5305\u542b\u8def\u7a0b\u65f6\u95f4\uff0c\u6298\u7b97\u6bcf\u79d2\u91c7\u96c6\u5230\u7684\u77ff\u77f3\u91cf", None))
#endif // QT_CONFIG(tooltip)
        self.MiningCountPerSecond.setText("")
#if QT_CONFIG(tooltip)
        self.RealProfitPerHour.setToolTip(QCoreApplication.translate("MainWindow", u"\u8003\u8651\u7206\u8239\u548c\u77ff\u77f3\u635f\u5931\uff0c\u6bcf\u5c0f\u65f6\u6240\u91c7\u77ff\u77f3\u7684\u6298\u7b97\u4ef7\u683c", None))
#endif // QT_CONFIG(tooltip)
        self.RealProfitPerHour.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u7406\u8bba\u6bcf\u5c0f\u65f6\u6536\u76ca", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u9645\u6bcf\u5c0f\u65f6\u6536\u76ca", None))
#if QT_CONFIG(tooltip)
        self.ProfitPerHourTheoretical.setToolTip(QCoreApplication.translate("MainWindow", u"\u5047\u8bbe\u4e0d\u7206\u8239\uff0c\u6bcf\u5c0f\u65f6\u6240\u91c7\u77ff\u77f3\u7684\u6298\u7b97\u4ef7\u683c", None))
#endif // QT_CONFIG(tooltip)
        self.ProfitPerHourTheoretical.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u7206\u8239\u98ce\u9669\u6298\u503c", None))
#if QT_CONFIG(tooltip)
        self.CrashRiskToMoney.setToolTip(QCoreApplication.translate("MainWindow", u"\u6309\u7167\u5f53\u524d\u7206\u8239\u7387\u548c\u77ff\u7269\u635f\u5931\u7387\uff0c\u5e73\u5747\u6bcf\u8f6e\u91c7\u77ff\u4e3a\u8230\u8239\u548c\u635f\u5931\u77ff\u77f3\u4ed8\u51fa\u7684\u6210\u672c", None))
#endif // QT_CONFIG(tooltip)
        self.CrashRiskToMoney.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u6ee1\u4ed3\u7b56\u7565", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u5355\u7a0b\u8017\u65f6", None))
#if QT_CONFIG(tooltip)
        self.TimeToSaveOrePoint.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4ece\u77ff\u533a\u5230\u7a7a\u95f4\u7ad9\u7684\u8def\u7a0b\u8017\u65f6\uff0c\u5305\u62ec\u9ad8\u4f4e\u5b89\u8dc3\u8fc1\u901f\u5ea6\u52a0\u6210</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.TimeToSaveOrePoint.setPrefix("")
        self.TimeToSaveOrePoint.setSuffix(QCoreApplication.translate("MainWindow", u" \u5206\u949f", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u653e\u77ff\u8017\u65f6", None))
#if QT_CONFIG(tooltip)
        self.TimeOfSaveOre.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4ece\u8fdb\u5165\u7a7a\u95f4\u7ad9\u5230\u5b8c\u6210\u5b58\u50a8\u51fa\u7ad9\u7684\u8017\u65f6</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.TimeOfSaveOre.setPrefix("")
        self.TimeOfSaveOre.setSuffix(QCoreApplication.translate("MainWindow", u" \u5206\u949f", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u5355\u7a0b\u8017\u65f6", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u62e5\u5835\u6307\u6570", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u5356\u77ff\u8017\u65f6", None))
#if QT_CONFIG(tooltip)
        self.CongestionIndex.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u8fdb\u5165\u8d38\u6613\u4e2d\u5fc3\u6240\u5728\u661f\u7cfb\u65f6\u9047\u5230\u62e5\u5835\u4ece\u800c\u5bfc\u81f4\u65f6\u95f4\u589e\u52a0\u7684\u6bd4\u4f8b\uff0c\u4ecb\u4e8e 0 \u5230 10 \u4e4b\u95f4</p><p>\u5982\u56e0\u5409\u4ed6\u62e5\u5835\u5bfc\u81f4\u9700\u8981\u7528 2 \u500d\u7684\u65f6\u95f4\u624d\u80fd\u8fdb\u5165\uff0c\u5219\u586b\u5165 2</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.TimeOfSellOre.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4ece\u8fdb\u5165\u8d38\u6613\u7a7a\u95f4\u7ad9\u5230\u5b8c\u6210\u51fa\u552e\u51fa\u7ad9\u7684\u8017\u65f6</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.TimeOfSellOre.setSuffix(QCoreApplication.translate("MainWindow", u" \u5206\u949f", None))
#if QT_CONFIG(tooltip)
        self.TimeToSellOrePoint.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4ece\u77ff\u533a\u5230\u8d38\u6613\u4e2d\u5fc3\u7a7a\u95f4\u7ad9\u7684\u8def\u7a0b\u8017\u65f6\uff0c\u5305\u62ec\u9ad8\u4f4e\u5b89\u8dc3\u8fc1\u901f\u5ea6\u52a0\u6210</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.TimeToSellOrePoint.setSuffix(QCoreApplication.translate("MainWindow", u" \u5206\u949f", None))
#if QT_CONFIG(tooltip)
        self.SellOreWhenFull.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ee1\u4ed3\u65f6\u5230\u8d38\u6613\u4e2d\u5fc3\u51fa\u552e\u77ff\u77f3\uff0c\u4e4b\u540e\u56de\u5230\u77ff\u533a\u7ee7\u7eed\u91c7\u77ff", None))
#endif // QT_CONFIG(tooltip)
        self.SellOreWhenFull.setText(QCoreApplication.translate("MainWindow", u"\u5356\u77ff", None))
#if QT_CONFIG(tooltip)
        self.SaveOreWhenFull.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ee1\u4ed3\u65f6\u56de\u5230\u7a7a\u95f4\u7ad9\u5c06\u77ff\u7269\u5b58\u50a8\uff0c\u7136\u540e\u56de\u5230\u77ff\u533a\u7ee7\u7eed\u91c7\u77ff", None))
#endif // QT_CONFIG(tooltip)
        self.SaveOreWhenFull.setText(QCoreApplication.translate("MainWindow", u"\u5b58\u77ff", None))
#if QT_CONFIG(tooltip)
        self.DropOreWhenFull.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ee1\u4ed3\u65f6\u5c06\u8d27\u7269\u629b\u5f03\u5230\u592a\u7a7a\u4e2d\u5e76\u7ee7\u7eed\u91c7\u77ff", None))
#endif // QT_CONFIG(tooltip)
        self.DropOreWhenFull.setText(QCoreApplication.translate("MainWindow", u"\u629b\u77ff", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u8f6f\u4ef6\u4f5c\u8005\uff1a\u521d\u5fc3\u4e0d\u53d8\u53f6\u5b50", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u7248\u672c\uff1a", None))
#if QT_CONFIG(tooltip)
        self.Version.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Version.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.Version.setText(QCoreApplication.translate("MainWindow", u"\u672a\u77e5", None))
#if QT_CONFIG(tooltip)
        self.CopyResult.setToolTip(QCoreApplication.translate("MainWindow", u"\u5c06\u8ba1\u7b97\u7ed3\u679c\u590d\u5236\u5230\u526a\u8d34\u677f", None))
#endif // QT_CONFIG(tooltip)
        self.CopyResult.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u7ed3\u679c", None))
#if QT_CONFIG(tooltip)
        self.Compute.setToolTip(QCoreApplication.translate("MainWindow", u"\u6839\u636e\u73b0\u6709\u6570\u636e\u8ba1\u7b97\u7ed3\u679c", None))
#endif // QT_CONFIG(tooltip)
        self.Compute.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
#if QT_CONFIG(tooltip)
        self.ClearAll.setToolTip(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u6240\u6709\u6570\u636e\u548c\u8ba1\u7b97\u7ed3\u679c", None))
#endif // QT_CONFIG(tooltip)
        self.ClearAll.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u6240\u6709", None))
    # retranslateUi
