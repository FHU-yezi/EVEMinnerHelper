import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from main_ui import Ui_MainWindow

try:
    from pyperclip import copy
except ImportError:
    pass

__version__ = "0.1.0"

ore_data = {
    "未知": 0.00, 
    "凡晶石": 0.1, 
    "灼烧岩": 0.15, 
    "干焦岩": 1.5, 
    "斜长岩": 0.35, 
    "奥贝尔石": 0.6, 
    "水硼砂": 1.2, 
    "杰斯贝矿": 4.0, 
    "希莫非特": 3.0, 
    "同位原矿": 3.0, 
    "灰岩": 3.2, 
    "黑赭石": 1.6, 
    "片麻岩": 2.0, 
    "克洛基石": 6.4, 
    "双多特石": 6.4, 
    "艾克诺岩": 6.4, 
    "基腹断岩": 8.0 
}

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.Version.setText(__version__)  # 显示版本号信息
        self.OreType.addItems(ore_data.keys())  # 将矿石信息添加到下拉框中
        
        self.OreType.currentTextChanged.connect(self.OreTypeChanged)  # 矿石种类变更时更新体积信息
        self.OreDataSettings.clicked.connect(self.OreDataManage)
        self.DropOreWhenFull.clicked.connect(self.ChoiceDropWhenFull)
        self.SaveOreWhenFull.clicked.connect(self.ChoiceSaveWhenFull)
        self.SellOreWhenFull.clicked.connect(self.ChoiceSellWhenFull)
        self.EnableCrashRisk.stateChanged.connect(self.CrashRiskCheckboxChanged)
        self.Compute.clicked.connect(self.ComputeData)
        self.ClearAll.clicked.connect(self.ClearAllData)
        self.CopyResult.clicked.connect(self.CopyToClipboard)
    
    def OreTypeChanged(self):
        now_type = self.OreType.currentText()
        self.OreVolume.setValue(ore_data[now_type])
        
    def OreDataManage(self):
        QMessageBox.information(self, "开发中", "该功能正在努力 Coding 中，敬请期待")
    
    def ChoiceDropWhenFull(self):
        """选择满仓抛矿时，调整其它满仓策略的数据输入框可用性
        """
        self.TimeToSaveOrePoint.setEnabled(False)
        self.TimeOfSaveOre.setEnabled(False)
        self.TimeToSellOrePoint.setEnabled(False)
        self.CongestionIndex.setEnabled(False)
        self.TimeOfSellOre.setEnabled(False)
        
    def ChoiceSaveWhenFull(self):
        """选择满仓存矿时，调整其它满仓策略的数据输入框可用性
        """
        self.TimeToSaveOrePoint.setEnabled(True)
        self.TimeOfSaveOre.setEnabled(True)
        self.TimeToSellOrePoint.setEnabled(False)
        self.CongestionIndex.setEnabled(False)
        self.TimeOfSellOre.setEnabled(False)
    
    def ChoiceSellWhenFull(self):
        """选择满仓卖矿时，调整其它满仓策略的数据输入框可用性
        """
        self.TimeToSaveOrePoint.setEnabled(False)
        self.TimeOfSaveOre.setEnabled(False)
        self.TimeToSellOrePoint.setEnabled(True)
        self.CongestionIndex.setEnabled(True)
        self.TimeOfSellOre.setEnabled(True)
    
    def CrashRiskCheckboxChanged(self):
        """爆船损失折算状态改变时，更新相关数据输入框的可用性
        """
        if self.EnableCrashRisk.isChecked() == True:
            self.CrashProbability.setEnabled(True)
            self.CrashOreLostProportion.setEnabled(True)
        else:
            self.CrashProbability.setEnabled(False)
            self.CrashOreLostProportion.setEnabled(False)
    
    def ClearAllData(self):
        """清空所有数据
        """
        self.OreVolume.setValue(0)
        self.OrePrice.setValue(0)
        self.ShipPrice.setValue(0)
        self.ShipCapacity.setValue(0)
        self.CrashProbability.setValue(0)
        self.CrashOreLostProportion.setValue(0)
        self.MiningVolumePerMachine.setValue(0)
        self.MiningMachineCount.setValue(0)
        self.TimePerMachineMining.setValue(0)
        self.MiningAdditionProportion.setValue(0)
        self.TimePerMachineMining.setValue(0)
        self.TimeProportionPerMining.setValue(0)
        self.TimeToSaveOrePoint.setValue(0)
        self.TimeOfSaveOre.setValue(0)
        self.TimeToSellOrePoint.setValue(0)
        self.CongestionIndex.setValue(0)
        self.TimeOfSellOre.setValue(0)
        
    def GetAllData(self):
        """返回用户填入的所有数据
        """
        result = {}
        result["OreVolume"] = self.OreVolume.value()
        result["OrePrice"] = self.OrePrice.value()
        result["ShipPrice"] = self.ShipPrice.value()
        result["ShipCapacity"] = self.ShipCapacity.value()
        result["CrashProbability"] = self.CrashProbability.value()
        result["CrashOreLostProportion"] = self.CrashOreLostProportion.value()
        result["MiningVolumePerMachine"] = self.MiningVolumePerMachine.value()
        result["MiningMachineCount"] = self.MiningMachineCount.value()
        result["TimePerMachineMining"] = self.TimePerMachineMining.value()
        result["MiningAdditionProportion"] = self.MiningAdditionProportion.value()
        result["TimeProportionPerMining"] = self.TimeProportionPerMining.value()
        if self.SaveOreWhenFull.isChecked():
            result["TimeToSaveOrePoint"] = self.TimeToSaveOrePoint.value()
            result["TimeOfSaveOre"] = self.TimeOfSaveOre.value()
        elif self.SellOreWhenFull.isChecked():
            result["TimeToSellOrePoint"] = self.TimeToSellOrePoint.value()
            result["CongestionIndex"] = self.CongestionIndex.value()
            result["TimeOfSellOre"] = self.TimeOfSellOre.value()
        return result
        
    
    def ComputeData(self):
        input_data = self.GetAllData()
        
        for key, value in input_data.items():
            # 除加成比例以外的其它数据不能为空
            if not value and key not in ["MiningAdditionProportion", "TimeProportionPerMining"]:
                QMessageBox.critical(self, "数据错误", "有数据未填写，请检查")
                return
        
        result = {}
        
        RealMiningVolumePerMachine = input_data["MiningVolumePerMachine"] * (1 + input_data["MiningAdditionProportion"])
        RealTimePerMachineMining = input_data["TimePerMachineMining"] * (1 - input_data["TimeProportionPerMining"])
        
        result["TimePerMining"] = round(input_data["ShipCapacity"] / (RealMiningVolumePerMachine * input_data["MiningMachineCount"] * \
                                  input_data["OreVolume"]) * RealTimePerMachineMining / 60, 1)
        if self.SaveOreWhenFull.isChecked():
            result["TimePerCycle"] = round(result["TimePerMining"] + 2 * input_data["TimeToSaveOrePoint"] + input_data["TimeOfSaveOre"], 1)
        elif self.SellOreWhenFull.isChecked():
            result["TimePerCycle"] = round(result["TimePerMining"] + 2 * input_data["TimeToSellOrePoint"] + input_data["TimeOfSellOre"], 1)
        else:
            result["TimePerCycle"] = result["TimePerMining"]
            
            
        result["CyclesCountPerHour"] = round(1 / result["TimePerCycle"] * 60, 2)
        result["MiningCountPerCycle"] = round(input_data["ShipCapacity"] / input_data["OreVolume"], 2)
        result["MiningCountPerSecond"] = round(result["MiningCountPerCycle"] / result["TimePerCycle"] / 60, 2)
        result["MiningCountPerHour"] = round(result["MiningCountPerSecond"] * 3600, 2)
        result["ProfitPerHourTheoretical"] = round(result["MiningCountPerHour"] * input_data["OrePrice"], 2)
        result["CrashRiskToMoney"] = round(input_data["ShipPrice"] * input_data["CrashProbability"] + \
                                     result["MiningCountPerCycle"] * input_data["CrashOreLostProportion"], 2)
        result["RealProfitPerHour"] = round(result["ProfitPerHourTheoretical"] - result["CrashRiskToMoney"], 2)
        self.UpdateResult(*result.values())
        
    
    def UpdateResult(self, TimePerMining, TimePerCycle, CyclesCountPerHour, 
                     MiningCountPerCycle, MiningCountPerSecond, MiningCountPerHour, 
                     ProfitPerHourTheoretical, CrashRiskToMoney, RealProfitPerHour):
        """更新计算结果
        """
        self.TimePerMining.setText(str(TimePerMining) + " 分钟")
        self.TimePerCycle.setText(str(TimePerCycle) + " 分钟")
        self.CyclesCountPerHour.setText(str(CyclesCountPerHour) + " 次")
        self.MiningCountPerCycle.setText(str(MiningCountPerCycle) + " m³")
        self.MiningCountPerSecond.setText(str(MiningCountPerSecond) + " m³")
        self.MiningCountPerHour.setText(str(MiningCountPerHour) + " m³")
        self.ProfitPerHourTheoretical.setText(str(ProfitPerHourTheoretical) + " ISK")
        self.CrashRiskToMoney.setText(str(CrashRiskToMoney) + " ISK")
        self.RealProfitPerHour.setText(str(RealProfitPerHour) + " ISK")
    
    def CopyToClipboard(self):
        try:
            copy("")
        except NameError:
            QMessageBox.critical(self, "依赖错误", "依赖库 PyPerclip 没有正确安装，该功能不可用")
            return
        
        if not self.TimePerMining.text():  # 没有计算结果
            QMessageBox.warning(self, "复制失败", "请先计算结果后再复制")
            return
        
        str_to_copy = ""
        data_to_copy = {}
        data_to_copy["矿石种类"] = str(self.OreType.currentText())
        data_to_copy["矿石体积"] = str(self.OreVolume.value()) + " m³"
        data_to_copy["矿石价值"] = str(self.OrePrice.value()) + " ISK"
        data_to_copy["舰船价值"] = str(self.ShipPrice.value()) + " ISK"
        data_to_copy["舰船容量"] = str(self.ShipCapacity.value()) + " m³"
        if self.EnableCrashRisk.isChecked():
            data_to_copy["预估爆船率"] = str(self.CrashProbability.value() * 100) + "%"
            data_to_copy["爆船矿物损失率"] = str(self.CrashOreLostProportion.value() * 100) + "%"
        data_to_copy["单次循环开采量"] = str(self.MiningCountPerCycle.text())
        data_to_copy["单次循环时间"] = str(self.TimePerCycle.text())
        data_to_copy["每仓开采耗时"] = str(self.TimePerMining.text())
        data_to_copy["每小时可开采"] = str(self.CyclesCountPerHour.text())
        data_to_copy["每秒开采量"] = str(self.MiningCountPerSecond.text())
        data_to_copy["每小时开采量"] = str(self.MiningCountPerSecond.text())
        data_to_copy["每小时收益"] = str(self.RealProfitPerHour.text())

        str_to_copy += "EVE 采矿方案：\n"
        
        for key, value in data_to_copy.items():
            str_to_copy += "".join([key, "：", value, "\n"])  # 使用 join 提高效率
        
        copy(str_to_copy)
        QMessageBox.information(self, "复制成功", "采矿方案已复制到剪贴板")
        
app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
