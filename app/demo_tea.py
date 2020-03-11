from PyQt5 import QtWidgets
import datetime
import sys
 
# Импортируем наш шаблон.
from viewsPy.demo_tea import Ui_MainWindow as demo_tea
import main as tea_welcome
 
class DemoTeaUI(QtWidgets.QMainWindow, demo_tea):
    def __init__(self):
        super(DemoTeaUI, self).__init__()
        self.setupUi(self)
        
        self.firstForemanDays = 0
        self.secondForemanDays = 0

        self.pushButton_73.clicked.connect(self.goToMenu)

        # коэффициент Еf
        self.pushButton_72.clicked.connect(self.toggleEf)
        self.label_138.hide()
        self.label_139.hide()
        self.label_140.hide()

        # setup first table
        for i in range(0, 9):

            item = QtWidgets.QDoubleSpinBox()
            value = float(self.tableWidget.item(i, 1).text())
            item.setRange(0, 1)
            item.setSingleStep(0.01)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeFirstTableValue)
            self.tableWidget.setCellWidget(i, 1, item)

            item = QtWidgets.QComboBox()
            value = int(self.tableWidget.item(i, 2).text())
            item.addItems(["1", "2", "3", "4", "5"])
            item.setCurrentIndex(value - 1)
            item.currentIndexChanged.connect(self.handleChangeFirstTable)
            self.tableWidget.setCellWidget(i, 2, item)

            item = QtWidgets.QComboBox()
            value = int(self.tableWidget.item(i, 3).text())
            item.addItems(["1", "2", "3", "4", "5"])
            item.setCurrentIndex(value - 1)
            item.currentIndexChanged.connect(self.handleChangeFirstTable)
            self.tableWidget.setCellWidget(i, 3, item)
        self.handleChangeFirstTable()

        # setup second table
        self.delimetrs = [0, 17, 22, 31]
        self.rowCount = 38
        self.isEven = False
        dateFrom = datetime.date.today()
        dateTo1 = datetime.date.today()
        dateTo2 = datetime.date.today()
        for i in range(0, self.rowCount):
            if (i in self.delimetrs):
                self.tableWidget_2.setSpan(i, 0, 1, 5)
                self.isEven = True
                continue

            if (self.isEven):
                self.tableWidget_2.setSpan(i, 0, 2, 1)
                item = QtWidgets.QTableWidgetItem()
                item.setText(str("Руководитель"))
                self.tableWidget_2.setItem(i, 1, item)
                item = QtWidgets.QSpinBox()
                value = int(self.tableWidget_2.item(i, 2).text())
                item.setValue(value)
                item.valueChanged.connect(self.handleChangeSecondTable)
                self.tableWidget_2.setCellWidget(i, 2, item)
                if (i == 1):
                    date = QtWidgets.QDateEdit()
                    date.setDate(dateFrom)
                    date.setDateRange(datetime.date.today(), datetime.date(3000, 12, 31))
                    date.dateChanged.connect(self.handleChangeSecondTable)
                    self.tableWidget_2.setCellWidget(i, 3, date)
                    dateTo = QtWidgets.QDateEdit()
                    dateTo.setDisabled(True)
                    days = int(self.tableWidget_2.item(i, 2).text()) - 1 if int(self.tableWidget_2.item(i, 2).text()) > 0 else 0
                    self.firstForemanDays += int(self.tableWidget_2.item(i, 2).text())
                    dateTo1 = dateFrom + datetime.timedelta(days = days)
                    dateTo.setDate(dateTo1)
                    self.tableWidget_2.setCellWidget(i, 4, dateTo)
                else:
                    date = QtWidgets.QDateEdit()
                    date.setDisabled(True)
                    date.setDate(dateFrom)
                    self.tableWidget_2.setCellWidget(i, 3, date)
                    dateTo = QtWidgets.QDateEdit()
                    dateTo.setDisabled(True)
                    days = int(self.tableWidget_2.item(i, 2).text()) - 1 if int(self.tableWidget_2.item(i, 2).text()) > 0 else 0
                    self.firstForemanDays += int(self.tableWidget_2.item(i, 2).text())
                    dateTo1 = dateFrom + datetime.timedelta(days = days)
                    dateTo.setDate(dateTo1)
                    self.tableWidget_2.setCellWidget(i, 4, dateTo)
            else:
                item = QtWidgets.QTableWidgetItem()
                item.setText(str("Программист"))
                self.tableWidget_2.setItem(i, 1, item)
                item = QtWidgets.QSpinBox()
                value = int(self.tableWidget_2.item(i, 2).text())
                item.setValue(value)
                item.valueChanged.connect(self.handleChangeSecondTable)
                self.tableWidget_2.setCellWidget(i, 2, item)
                date = QtWidgets.QDateEdit()
                date.setDisabled(True)
                date.setDate(dateFrom)
                self.tableWidget_2.setCellWidget(i, 3, date)
                dateTo = QtWidgets.QDateEdit()
                dateTo.setDisabled(True)
                days = int(self.tableWidget_2.item(i, 2).text()) - 1 if int(self.tableWidget_2.item(i, 2).text()) > 0 else 0
                self.secondForemanDays += int(self.tableWidget_2.item(i, 2).text())
                dateTo2 = dateFrom + datetime.timedelta(days = days)
                dateTo.setDate(dateTo2)
                self.tableWidget_2.setCellWidget(i, 4, dateTo)
            self.isEven = not self.isEven
            if (dateTo1 > dateTo2):
                dateFrom = dateTo1
            else:
                dateFrom = dateTo2

        # setup third table
        self.pushButton_15.clicked.connect(self.addMaterial)
        for i in range(self.tableWidget_3.rowCount()):
            value = self.tableWidget_3.item(i, 2).text()
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(float(value))
            item.valueChanged.connect(self.handleChangeThirdTable)
            self.tableWidget_3.setCellWidget(i, 2, item)
            value = self.tableWidget_3.item(i, 3).text()
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(float(value))
            item.valueChanged.connect(self.handleChangeThirdTable)
            self.tableWidget_3.setCellWidget(i, 3, item)

        # настройка 4 таблицы
        self.pushButton_20.clicked.connect(self.addEquipment)
        self.spinBox.editingFinished.connect(self.handleChangeWorkingDayPerYear)
        self.workingDayPerYear = self.spinBox.value()
        # self.workingHoursPerDay = round((self.timeEdit_2.minute() + self.timeEdit_2.hour() * 60) / 60, 2)
        for i in range(0, self.tableWidget_4.rowCount()):
            value = int(self.tableWidget_4.item(i, 1).text())
            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeFourTable)
            self.tableWidget_4.setCellWidget(i, 1, item)

            value = float(self.tableWidget_4.item(i, 2).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeFourTable)
            self.tableWidget_4.setCellWidget(i, 2, item)

            value = float(self.tableWidget_4.item(i, 3).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1)
            item.setSingleStep(0.1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeFourTable)
            self.tableWidget_4.setCellWidget(i, 3, item)

            value = int(self.tableWidget_4.item(i, 4).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeFourTable)
            self.tableWidget_4.setCellWidget(i, 4, item)

            item = QtWidgets.QTimeEdit()
            item.setTime(datetime.time(8, 0))
            item.editingFinished.connect(self.handleChangeFourTable)
            self.tableWidget_4.setCellWidget(i, 5, item)

            item = QtWidgets.QTimeEdit()
            item.setTime(datetime.time(6, 0))
            item.editingFinished.connect(self.handleChangeFourTable)
            self.tableWidget_4.setCellWidget(i, 6, item)

            value = int(self.tableWidget_4.item(i, 7).text())
            item = QtWidgets.QSpinBox()
            item.setRange(0, 366)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeFourTable)
            self.tableWidget_4.setCellWidget(i, 7, item)

        # настройка 5 таблицы
        self.pushButton_25.clicked.connect(self.addBuilding)
        for i in range(0, self.tableWidget_5.rowCount()):
            value = int(self.tableWidget_5.item(i, 1).text())
            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeFiveTable)
            self.tableWidget_5.setCellWidget(i, 1, item)

            value = int(self.tableWidget_5.item(i, 2).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeFiveTable)
            self.tableWidget_5.setCellWidget(i, 2, item)

        # настройка 6 таблицы
        self.pushButton_26.clicked.connect(self.addPackage)
        for i in range(0, self.tableWidget_6.rowCount()):
            value = int(self.tableWidget_6.item(i, 1).text())
            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeSixTable)
            self.tableWidget_6.setCellWidget(i, 1, item)

            value = int(self.tableWidget_6.item(i, 2).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeSixTable)
            self.tableWidget_6.setCellWidget(i, 2, item)
        # настройка 7 таблицы
        self.pushButton_31.clicked.connect(self.addConnectionLine)
        for i in range(0, self.tableWidget_7.rowCount()):
            value = int(self.tableWidget_7.item(i, 1).text())
            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeSevenTable)
            self.tableWidget_7.setCellWidget(i, 1, item)

            value = int(self.tableWidget_7.item(i, 2).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeSevenTable)
            self.tableWidget_7.setCellWidget(i, 2, item)

        # настройка 8 таблицы
        self.pushButton_34.clicked.connect(self.addInfoBase)
        for i in range(0, self.tableWidget_8.rowCount()):
            value = int(self.tableWidget_8.item(i, 1).text())
            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeEightTable)
            self.tableWidget_8.setCellWidget(i, 1, item)

            value = int(self.tableWidget_8.item(i, 2).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeEightTable)
            self.tableWidget_8.setCellWidget(i, 2, item)
        # настройка 9 таблицы
        self.pushButton_35.clicked.connect(self.addTraining)
        for i in range(0, self.tableWidget_9.rowCount()):
            value = int(self.tableWidget_9.item(i, 1).text())
            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeNineTable)
            self.tableWidget_9.setCellWidget(i, 1, item)

            value = int(self.tableWidget_9.item(i, 2).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeNineTable)
            self.tableWidget_9.setCellWidget(i, 2, item)

        # настройка 10 таблицы
        self.pushButton_38.clicked.connect(self.addAnalEquipment)
        for i in range(0, self.tableWidget_10.rowCount()):
            value = int(self.tableWidget_10.item(i, 1).text())
            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeTenTable)
            self.tableWidget_10.setCellWidget(i, 1, item)

            value = float(self.tableWidget_10.item(i, 2).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeTenTable)
            self.tableWidget_10.setCellWidget(i, 2, item)

            value = float(self.tableWidget_10.item(i, 3).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1)
            item.setSingleStep(0.1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeTenTable)
            self.tableWidget_10.setCellWidget(i, 3, item)

            value = int(self.tableWidget_10.item(i, 4).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeTenTable)
            self.tableWidget_10.setCellWidget(i, 4, item)

            item = QtWidgets.QTimeEdit()
            item.setTime(datetime.time(8, 0))
            item.editingFinished.connect(self.handleChangeTenTable)
            self.tableWidget_10.setCellWidget(i, 5, item)

            item = QtWidgets.QTimeEdit()
            item.setTime(datetime.time(6, 0))
            item.editingFinished.connect(self.handleChangeTenTable)
            self.tableWidget_10.setCellWidget(i, 6, item)

            value = int(self.tableWidget_10.item(i, 7).text())
            item = QtWidgets.QSpinBox()
            item.setRange(0, 366)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeTenTable)
            self.tableWidget_10.setCellWidget(i, 7, item)

        # Настройка 11 таблицы
        self.pushButton_45.clicked.connect(self.addProjStuff)
        for i in range(0, self.tableWidget_11.rowCount()):
            value = float(self.tableWidget_11.item(i, 1).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeElevenTable)
            self.tableWidget_11.setCellWidget(i, 1, item)

            value = float(self.tableWidget_11.item(i, 2).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeElevenTable)
            self.tableWidget_11.setCellWidget(i, 2, item)

        # настройка 12 таблицы
        self.pushButton_48.clicked.connect(self.addAnalStuff)
        for i in range(0, self.tableWidget_12.rowCount()):
            value = float(self.tableWidget_12.item(i, 1).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeTwelveTable)
            self.tableWidget_12.setCellWidget(i, 1, item)

            value = float(self.tableWidget_12.item(i, 2).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChangeTwelveTable)
            self.tableWidget_12.setCellWidget(i, 2, item)

        self.doubleSpinBox_23.valueChanged.connect(self.handleChangeRayounniyCoeff)


        # настройка 13 таблицы
        self.pushButton_51.clicked.connect(self.addAnal2)
        for i in range(0, self.tableWidget_13.rowCount()):
            value = float(self.tableWidget_13.item(i, 1).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChange13Table)
            self.tableWidget_13.setCellWidget(i, 1, item)

            value = float(self.tableWidget_13.item(i, 2).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChange13Table)
            self.tableWidget_13.setCellWidget(i, 2, item)

        # настройка 14 таблицы
        self.pushButton_54.clicked.connect(self.addAnal3)
        for i in range(0, self.tableWidget_14.rowCount()):
            value = float(self.tableWidget_14.item(i, 1).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChange14Table)
            self.tableWidget_14.setCellWidget(i, 1, item)

            value = float(self.tableWidget_14.item(i, 2).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChange14Table)
            self.tableWidget_14.setCellWidget(i, 2, item)

        # настройка 15 таблицы
        self.pushButton_59.clicked.connect(self.addAnal4)
        for i in range(0, self.tableWidget_15.rowCount()):
            value = float(self.tableWidget_15.item(i, 1).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChange15Table)
            self.tableWidget_15.setCellWidget(i, 1, item)

            value = float(self.tableWidget_15.item(i, 2).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChange15Table)
            self.tableWidget_15.setCellWidget(i, 2, item)

        # настройка 16 таблицы
        self.pushButton_60.clicked.connect(self.addAnal5)
        for i in range(0, self.tableWidget_16.rowCount()):
            value = float(self.tableWidget_16.item(i, 1).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChange16Table)
            self.tableWidget_16.setCellWidget(i, 1, item)

            value = float(self.tableWidget_16.item(i, 2).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChange16Table)
            self.tableWidget_16.setCellWidget(i, 2, item)

        # настройка 17 таблицы
        self.pushButton_65.clicked.connect(self.addAnal6)
        for i in range(0, self.tableWidget_17.rowCount()):
            value = float(self.tableWidget_17.item(i, 1).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChange17Table)
            self.tableWidget_17.setCellWidget(i, 1, item)

            value = float(self.tableWidget_17.item(i, 2).text())
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(value)
            item.valueChanged.connect(self.handleChange17Table)
            self.tableWidget_17.setCellWidget(i, 2, item)

        # setup KTS label 
        self.label_21.hide()
        self.pushButton.clicked.connect(self.toggleKTS)

        # buttons to next tab
        self.pushButton_2.clicked.connect(self.nextTab)
        self.pushButton_4.clicked.connect(self.nextTab)
        self.pushButton_6.clicked.connect(self.nextTab)
        self.pushButton_8.clicked.connect(self.nextTab)
        self.pushButton_11.clicked.connect(self.nextTab)
        self.pushButton_13.clicked.connect(self.nextTab)
        self.pushButton_16.clicked.connect(self.nextTab)
        self.pushButton_19.clicked.connect(self.nextTab)
        self.pushButton_22.clicked.connect(self.nextTab)
        self.pushButton_24.clicked.connect(self.nextTab)
        self.pushButton_28.clicked.connect(self.nextTab)
        self.pushButton_30.clicked.connect(self.nextTab)
        self.pushButton_33.clicked.connect(self.nextTab)
        self.pushButton_37.clicked.connect(self.nextTab)
        self.pushButton_40.clicked.connect(self.nextTab)
        self.pushButton_53.clicked.connect(self.nextTab)
        self.pushButton_56.clicked.connect(self.nextTab)
        self.pushButton_58.clicked.connect(self.nextTab)
        self.pushButton_62.clicked.connect(self.nextTab)
        self.pushButton_64.clicked.connect(self.nextTab)
        self.pushButton_41.clicked.connect(self.nextTab)
        self.pushButton_67.clicked.connect(self.nextTab)
        self.pushButton_43.clicked.connect(self.nextTab)
        self.pushButton_47.clicked.connect(self.nextTab)
        self.pushButton_50.clicked.connect(self.nextTab)
        self.pushButton_69.clicked.connect(self.nextTab)
        self.pushButton_70.clicked.connect(self.nextTab)
        self.pushButton_76.clicked.connect(self.nextTab)

        # buttons to prev tab
        self.pushButton_5.clicked.connect(self.prevTab)
        self.pushButton_9.clicked.connect(self.prevTab)
        self.pushButton_10.clicked.connect(self.prevTab)
        self.pushButton_12.clicked.connect(self.prevTab)
        self.pushButton_14.clicked.connect(self.prevTab)
        self.pushButton_17.clicked.connect(self.prevTab)
        self.pushButton_18.clicked.connect(self.prevTab)
        self.pushButton_21.clicked.connect(self.prevTab)
        self.pushButton_23.clicked.connect(self.prevTab)
        self.pushButton_27.clicked.connect(self.prevTab)
        self.pushButton_29.clicked.connect(self.prevTab)
        self.pushButton_32.clicked.connect(self.prevTab)
        self.pushButton_36.clicked.connect(self.prevTab)
        self.pushButton_39.clicked.connect(self.prevTab)
        self.pushButton_52.clicked.connect(self.prevTab)
        self.pushButton_55.clicked.connect(self.prevTab)
        self.pushButton_57.clicked.connect(self.prevTab)
        self.pushButton_61.clicked.connect(self.prevTab)
        self.pushButton_63.clicked.connect(self.prevTab)
        self.pushButton_42.clicked.connect(self.prevTab)
        self.pushButton_66.clicked.connect(self.prevTab)
        self.pushButton_44.clicked.connect(self.prevTab)
        self.pushButton_46.clicked.connect(self.prevTab)
        self.pushButton_49.clicked.connect(self.prevTab)
        self.pushButton_68.clicked.connect(self.prevTab)
        self.pushButton_71.clicked.connect(self.prevTab)
        self.pushButton_74.clicked.connect(self.prevTab)
        self.pushButton_75.clicked.connect(self.prevTab)

        # button to add PK(Показатель качества)
        self.pushButton_3.clicked.connect(self.addPK)

        # check tab index
        self.tabWidget.currentChanged.connect(self.handleChangeTabIndex)

        # self.pushButton_73.clicked.connect(self.toMenu)

    def handleChangeRayounniyCoeff(self):
        self.handleChangeElevenTable()
        self.handleChangeTwelveTable()

    def addAnal6(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Добавить',
            'Введите название:')
        if ok: 
            rowIndex = self.tableWidget_17.rowCount()
            item = QtWidgets.QTableWidgetItem()
            item.setText(text)
            self.tableWidget_17.insertRow(rowIndex)
            self.tableWidget_17.setItem(rowIndex, 0, item)

            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChange17Table)
            self.tableWidget_17.setCellWidget(rowIndex, 1, item)

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChange17Table)
            self.tableWidget_17.setCellWidget(rowIndex, 2, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(str(0))
            self.tableWidget_17.setItem(rowIndex, 3, item)

    def handleChange17Table(self):
        sumTotal = 0
        for i in range(self.tableWidget_17.rowCount()):
            count = int(self.tableWidget_17.cellWidget(i, 1).value())
            cost = float(self.tableWidget_17.cellWidget(i, 2).value())
            total = 0
            total = round(cost * count, 2)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(total))
            self.tableWidget_17.setItem(i, 3, item)
            sumTotal += total

        self.label_51.setText(str(round(sumTotal, 2)))

    def addAnal5(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Добавить информационную базу',
            'Введите название:')
        if ok: 
            rowIndex = self.tableWidget_16.rowCount()
            item = QtWidgets.QTableWidgetItem()
            item.setText(text)
            self.tableWidget_16.insertRow(rowIndex)
            self.tableWidget_16.setItem(rowIndex, 0, item)

            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChange16Table)
            self.tableWidget_16.setCellWidget(rowIndex, 1, item)

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChange16Table)
            self.tableWidget_16.setCellWidget(rowIndex, 2, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(str(0))
            self.tableWidget_16.setItem(rowIndex, 3, item)

    def handleChange16Table(self):
        sumTotal = 0
        for i in range(self.tableWidget_16.rowCount()):
            count = int(self.tableWidget_16.cellWidget(i, 1).value())
            cost = float(self.tableWidget_16.cellWidget(i, 2).value())
            total = 0
            total = round(cost * count, 2)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(total))
            self.tableWidget_16.setItem(i, 3, item)
            sumTotal += total

        self.label_49.setText(str(round(sumTotal, 2)))

    def addAnal4(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Добавить линию связи',
            'Введите название:')
        if ok: 
            rowIndex = self.tableWidget_15.rowCount()
            item = QtWidgets.QTableWidgetItem()
            item.setText(text)
            self.tableWidget_15.insertRow(rowIndex)
            self.tableWidget_15.setItem(rowIndex, 0, item)

            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChange15Table)
            self.tableWidget_15.setCellWidget(rowIndex, 1, item)

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChange15Table)
            self.tableWidget_15.setCellWidget(rowIndex, 2, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(str(0))
            self.tableWidget_15.setItem(rowIndex, 3, item)

    def handleChange15Table(self):
        sumTotal = 0
        for i in range(self.tableWidget_15.rowCount()):
            count = int(self.tableWidget_15.cellWidget(i, 1).value())
            cost = float(self.tableWidget_15.cellWidget(i, 2).value())
            total = 0
            total = round(cost * count, 2)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(total))
            self.tableWidget_15.setItem(i, 3, item)
            sumTotal += total

        self.label_47.setText(str(round(sumTotal, 2)))

    def addAnal3(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Добавить разработку',
            'Введите название:')
        if ok: 
            rowIndex = self.tableWidget_14.rowCount()
            item = QtWidgets.QTableWidgetItem()
            item.setText(text)
            self.tableWidget_14.insertRow(rowIndex)
            self.tableWidget_14.setItem(rowIndex, 0, item)

            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChange14Table)
            self.tableWidget_14.setCellWidget(rowIndex, 1, item)

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChange14Table)
            self.tableWidget_14.setCellWidget(rowIndex, 2, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(str(0))
            self.tableWidget_14.setItem(rowIndex, 3, item)

    def handleChange14Table(self):
        sumTotal = 0
        for i in range(self.tableWidget_14.rowCount()):
            count = int(self.tableWidget_14.cellWidget(i, 1).value())
            cost = float(self.tableWidget_14.cellWidget(i, 2).value())
            total = 0
            total = round(cost * count, 2)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(total))
            self.tableWidget_14.setItem(i, 3, item)
            sumTotal += total

        self.label_43.setText(str(round(sumTotal, 2)))

    def addAnal2(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Добавить услугу',
            'Введите название услугу:')
        if ok: 
            rowIndex = self.tableWidget_13.rowCount()
            item = QtWidgets.QTableWidgetItem()
            item.setText(text)
            self.tableWidget_13.insertRow(rowIndex)
            self.tableWidget_13.setItem(rowIndex, 0, item)

            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChange13Table)
            self.tableWidget_13.setCellWidget(rowIndex, 1, item)

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChange13Table)
            self.tableWidget_13.setCellWidget(rowIndex, 2, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(str(0))
            self.tableWidget_13.setItem(rowIndex, 3, item)

    def handleChange13Table(self):
        sumTotal = 0
        for i in range(self.tableWidget_13.rowCount()):
            count = int(self.tableWidget_13.cellWidget(i, 1).value())
            cost = float(self.tableWidget_13.cellWidget(i, 2).value())
            total = 0
            total = round(cost * count, 2)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(total))
            self.tableWidget_13.setItem(i, 3, item)
            sumTotal += total

        self.label_41.setText(str(round(sumTotal, 2)))

    def addAnalStuff(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Добавить должность',
            'Введите название:')
        if ok: 
            rowIndex = self.tableWidget_12.rowCount()
            item = QtWidgets.QTableWidgetItem()
            item.setText(text)
            self.tableWidget_12.insertRow(rowIndex)
            self.tableWidget_12.setItem(rowIndex, 0, item)

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeTwelveTable)
            self.tableWidget_12.setCellWidget(rowIndex, 1, item)

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeTwelveTable)
            self.tableWidget_12.setCellWidget(rowIndex, 2, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(str(0))
            self.tableWidget_12.setItem(rowIndex, 3, item)

    def handleChangeTwelveTable(self):
        sumTotal = 0
        for i in range(self.tableWidget_12.rowCount()):
            cost = round(float(self.tableWidget_12.cellWidget(i, 1).value()) / 21, 2)
            days = float(self.tableWidget_12.cellWidget(i, 2).value())
            total = 0
            total = round(cost * days, 2)
            
            socialKf = self.doubleSpinBox_15.value() + self.doubleSpinBox_16.value() + self.doubleSpinBox_17.value() + self.doubleSpinBox_18.value()
            additionalKf = self.doubleSpinBox_13.value() + self.doubleSpinBox_23.value()

            result = round(total * (1 + additionalKf) * (1 + socialKf), 2)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(result))
            self.tableWidget_12.setItem(i, 3, item)
            sumTotal += result

        self.label_39.setText(str(round(sumTotal, 2)))

    def addProjStuff(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Добавить должность',
            'Введите название:')
        if ok: 
            rowIndex = self.tableWidget_11.rowCount()
            item = QtWidgets.QTableWidgetItem()
            item.setText(text)
            self.tableWidget_11.insertRow(rowIndex)
            self.tableWidget_11.setItem(rowIndex, 0, item)

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeElevenTable)
            self.tableWidget_11.setCellWidget(rowIndex, 1, item)

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeElevenTable)
            self.tableWidget_11.setCellWidget(rowIndex, 2, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(str(0))
            self.tableWidget_11.setItem(rowIndex, 3, item)

    def handleChangeElevenTable(self):
        sumTotal = 0
        for i in range(self.tableWidget_11.rowCount()):
            cost = round(float(self.tableWidget_11.cellWidget(i, 1).value()) / 21, 2)
            days = float(self.tableWidget_11.cellWidget(i, 2).value())
            total = 0
            total = round(cost * days, 2)
            
            socialKf = self.doubleSpinBox_15.value() + self.doubleSpinBox_16.value() + self.doubleSpinBox_17.value() + self.doubleSpinBox_18.value()
            additionalKf = self.doubleSpinBox_13.value() + self.doubleSpinBox_23.value()

            result = round(total * (1 + additionalKf) * (1 + socialKf), 2)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(result))
            self.tableWidget_11.setItem(i, 3, item)
            sumTotal += result

        self.label_36.setText(str(round(sumTotal, 2)))

    def addAnalEquipment(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Добавить оборудование для аналога',
            'Введите название оборудования:')
        if ok:  
            rowIndex = self.tableWidget_10.rowCount()
            item = QtWidgets.QTableWidgetItem()
            item.setText(text)
            self.tableWidget_10.insertRow(rowIndex)
            self.tableWidget_10.setItem(rowIndex, 0, item)

            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeTenTable)
            self.tableWidget_10.setCellWidget(rowIndex, 1, item)

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeTenTable)
            self.tableWidget_10.setCellWidget(rowIndex, 2, item) 

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1)
            item.setSingleStep(0.1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeTenTable)
            self.tableWidget_10.setCellWidget(rowIndex, 3, item) 

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeTenTable)
            self.tableWidget_10.setCellWidget(rowIndex, 4, item)

            item = QtWidgets.QTimeEdit()
            item.setTime(datetime.time(0, 0))
            item.editingFinished.connect(self.handleChangeTenTable)
            self.tableWidget_10.setCellWidget(rowIndex, 5, item)

            item = QtWidgets.QTimeEdit()
            item.setTime(datetime.time(0, 0))
            item.editingFinished.connect(self.handleChangeTenTable)
            self.tableWidget_10.setCellWidget(rowIndex, 6, item)

            item = QtWidgets.QSpinBox()
            item.setRange(0, 366)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeTenTable)
            self.tableWidget_10.setCellWidget(rowIndex, 7, item)

            item = QtWidgets.QSpinBox()
            item.setRange(0, 100)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeTenTable)
            self.tableWidget_10.setCellWidget(rowIndex, 8, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(str(0))
            self.tableWidget_10.setItem(rowIndex, 9, item)

    def handleChangeTenTable(self):
        sumTotal = 0
        for i in range(self.tableWidget_10.rowCount()):
            count = int(self.tableWidget_10.cellWidget(i, 1).value())
            cost = float(self.tableWidget_10.cellWidget(i, 4).value())
            usingHours = (self.tableWidget_10.cellWidget(i, 5).time().minute() + (self.tableWidget_10.cellWidget(i, 5).time().hour() * 60)) / 60
            hoursPerTask = (self.tableWidget_10.cellWidget(i, 6).time().minute() + (self.tableWidget_10.cellWidget(i, 6).time().hour() * 60)) / 60
            days = self.tableWidget_10.cellWidget(i, 7).value()

            delimetr = (days * usingHours)
            total = 0
            if (delimetr != 0):
                total = round(cost * count * ((hoursPerTask * self.workingDayPerYear) / delimetr), 2)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(total))
            self.tableWidget_10.setItem(i, 9, item)
            sumTotal += total

        self.label_25.setText(str(round(sumTotal, 2)))

    def addTraining(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Добавить затраты на обучение персонала',
            'Введите название:')
        if ok: 
            rowIndex = self.tableWidget_9.rowCount()
            item = QtWidgets.QTableWidgetItem()
            item.setText(text)
            self.tableWidget_9.insertRow(rowIndex)
            self.tableWidget_9.setItem(rowIndex, 0, item)

            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeNineTable)
            self.tableWidget_9.setCellWidget(rowIndex, 1, item)

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeNineTable)
            self.tableWidget_9.setCellWidget(rowIndex, 2, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(str(0))
            self.tableWidget_9.setItem(rowIndex, 3, item)

    def handleChangeNineTable(self):
        sumTotal = 0
        for i in range(self.tableWidget_9.rowCount()):
            count = int(self.tableWidget_9.cellWidget(i, 1).value())
            cost = float(self.tableWidget_9.cellWidget(i, 2).value())
            total = 0
            total = round(cost * count, 2)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(total))
            self.tableWidget_9.setItem(i, 3, item)
            sumTotal += total

        self.label_23.setText(str(round(sumTotal, 2)))

    def addInfoBase(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Добавить информационную базу',
            'Введите название:')
        if ok: 
            rowIndex = self.tableWidget_8.rowCount()
            item = QtWidgets.QTableWidgetItem()
            item.setText(text)
            self.tableWidget_8.insertRow(rowIndex)
            self.tableWidget_8.setItem(rowIndex, 0, item)

            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeEightTable)
            self.tableWidget_8.setCellWidget(rowIndex, 1, item)

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeEightTable)
            self.tableWidget_8.setCellWidget(rowIndex, 2, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(str(0))
            self.tableWidget_8.setItem(rowIndex, 3, item)

    def handleChangeEightTable(self):
        sumTotal = 0
        for i in range(self.tableWidget_8.rowCount()):
            count = int(self.tableWidget_8.cellWidget(i, 1).value())
            cost = float(self.tableWidget_8.cellWidget(i, 2).value())
            total = 0
            total = round(cost * count, 2)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(total))
            self.tableWidget_8.setItem(i, 3, item)
            sumTotal += total

        self.label_13.setText(str(round(sumTotal, 2)))

    def addConnectionLine(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Добавить линию связи',
            'Введите название:')
        if ok: 
            rowIndex = self.tableWidget_7.rowCount()
            item = QtWidgets.QTableWidgetItem()
            item.setText(text)
            self.tableWidget_7.insertRow(rowIndex)
            self.tableWidget_7.setItem(rowIndex, 0, item)

            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeSevenTable)
            self.tableWidget_7.setCellWidget(rowIndex, 1, item)

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeSevenTable)
            self.tableWidget_7.setCellWidget(rowIndex, 2, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(str(0))
            self.tableWidget_7.setItem(rowIndex, 3, item)

    def handleChangeSevenTable(self):
        sumTotal = 0
        for i in range(self.tableWidget_7.rowCount()):
            count = int(self.tableWidget_7.cellWidget(i, 1).value())
            cost = float(self.tableWidget_7.cellWidget(i, 2).value())
            total = 0
            total = round(cost * count, 2)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(total))
            self.tableWidget_7.setItem(i, 3, item)
            sumTotal += total

        self.label_11.setText(str(round(sumTotal, 2)))

    def addPackage(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Добавить пакет/разработку',
            'Введите название:')
        if ok: 
            rowIndex = self.tableWidget_6.rowCount()
            item = QtWidgets.QTableWidgetItem()
            item.setText(text)
            self.tableWidget_6.insertRow(rowIndex)
            self.tableWidget_6.setItem(rowIndex, 0, item)

            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeSixTable)
            self.tableWidget_6.setCellWidget(rowIndex, 1, item)

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeSixTable)
            self.tableWidget_6.setCellWidget(rowIndex, 2, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(str(0))
            self.tableWidget_6.setItem(rowIndex, 3, item)

    def handleChangeSixTable(self):
        sumTotal = 0
        for i in range(self.tableWidget_6.rowCount()):
            count = int(self.tableWidget_6.cellWidget(i, 1).value())
            cost = float(self.tableWidget_6.cellWidget(i, 2).value())
            total = 0
            total = round(cost * count, 2)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(total))
            self.tableWidget_6.setItem(i, 3, item)
            sumTotal += total

        self.label_9.setText(str(round(sumTotal, 2)))

    def addBuilding(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Добавить услугу',
            'Введите название услугу:')
        if ok: 
            rowIndex = self.tableWidget_5.rowCount()
            item = QtWidgets.QTableWidgetItem()
            item.setText(text)
            self.tableWidget_5.insertRow(rowIndex)
            self.tableWidget_5.setItem(rowIndex, 0, item)

            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeFiveTable)
            self.tableWidget_5.setCellWidget(rowIndex, 1, item)

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeFiveTable)
            self.tableWidget_5.setCellWidget(rowIndex, 2, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(str(0))
            self.tableWidget_5.setItem(rowIndex, 3, item)

    def handleChangeFiveTable(self):
        sumTotal = 0
        for i in range(self.tableWidget_5.rowCount()):
            count = int(self.tableWidget_5.cellWidget(i, 1).value())
            cost = float(self.tableWidget_5.cellWidget(i, 2).value())
            total = 0
            total = round(cost * count, 2)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(total))
            self.tableWidget_5.setItem(i, 3, item)
            sumTotal += total

        self.label_7.setText(str(round(sumTotal, 2)))

    def addEquipment(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Добавить оборудование',
            'Введите название оборудования:')
        if ok: 
            rowIndex = self.tableWidget_4.rowCount()
            item = QtWidgets.QTableWidgetItem()
            item.setText(text)
            self.tableWidget_4.insertRow(rowIndex)
            self.tableWidget_4.setItem(rowIndex, 0, item)

            item = QtWidgets.QSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeFourTable)
            self.tableWidget_4.setCellWidget(rowIndex, 1, item)

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeFourTable)
            self.tableWidget_4.setCellWidget(rowIndex, 2, item) 

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1)
            item.setSingleStep(0.1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeFourTable)
            self.tableWidget_4.setCellWidget(rowIndex, 3, item) 

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeFourTable)
            self.tableWidget_4.setCellWidget(rowIndex, 4, item)

            item = QtWidgets.QTimeEdit()
            item.setTime(datetime.time(0, 0))
            item.editingFinished.connect(self.handleChangeFourTable)
            self.tableWidget_4.setCellWidget(rowIndex, 5, item)

            item = QtWidgets.QTimeEdit()
            item.setTime(datetime.time(0, 0))
            item.editingFinished.connect(self.handleChangeFourTable)
            self.tableWidget_4.setCellWidget(rowIndex, 6, item)

            item = QtWidgets.QSpinBox()
            item.setRange(0, 366)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeFourTable)
            self.tableWidget_4.setCellWidget(rowIndex, 7, item)

            item = QtWidgets.QSpinBox()
            item.setRange(0, 100)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeFourTable)
            self.tableWidget_4.setCellWidget(rowIndex, 8, item)

            item = QtWidgets.QTableWidgetItem()
            item.setText(str(0))
            self.tableWidget_4.setItem(rowIndex, 9, item)

    def addMaterial(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Добавить материал',
            'Введите название материала:')
        if ok: 
            rowIndex = self.tableWidget_3.rowCount()
            self.tableWidget_3.insertRow(rowIndex)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(text))
            self.tableWidget_3.setItem(rowIndex, 0, item)
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeThirdTable)
            self.tableWidget_3.setCellWidget(rowIndex, 2, item)
            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1000000000)
            item.setSingleStep(1)
            item.setValue(0)
            item.valueChanged.connect(self.handleChangeThirdTable)
            self.tableWidget_3.setCellWidget(rowIndex, 3, item)

    def handleChangeWorkingDayPerYear(self):
        self.workingDayPerYear = self.spinBox.value()
        self.handleChangeFourTable()

    def handleChangeFourTable(self):
        sumTotal = 0
        for i in range(self.tableWidget_4.rowCount()):
            count = int(self.tableWidget_4.cellWidget(i, 1).value())
            cost = float(self.tableWidget_4.cellWidget(i, 4).value())
            usingHours = (self.tableWidget_4.cellWidget(i, 5).time().minute() + (self.tableWidget_4.cellWidget(i, 5).time().hour() * 60)) / 60
            hoursPerTask = (self.tableWidget_4.cellWidget(i, 6).time().minute() + (self.tableWidget_4.cellWidget(i, 6).time().hour() * 60)) / 60
            days = self.tableWidget_4.cellWidget(i, 7).value()

            delimetr = (days * usingHours)
            total = 0
            if (delimetr != 0):
                total = round(cost * count * ((hoursPerTask * self.workingDayPerYear) / delimetr), 2)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(total))
            self.tableWidget_4.setItem(i, 9, item)
            sumTotal += total

        self.label_5.setText(str(round(sumTotal, 2)))

    def handleChangeThirdTable(self):
        sum = 0
        for i in range(self.tableWidget_3.rowCount()):
            count = float(self.tableWidget_3.cellWidget(i, 2).value())
            cost  = float(self.tableWidget_3.cellWidget(i, 3).value())
            value = round(count * cost, 2)
            sum += value
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(value))
            self.tableWidget_3.setItem(i, 4, item)
        self.label_2.setText(str(round(sum, 2)))

    def getFirstResult(self):
        # main salary
        firstForemanSalary = self.doubleSpinBox_11.value() / 21 * self.firstForemanDays
        secondForemanSalary = self.doubleSpinBox_12.value() / 21 * self.secondForemanDays
        summaryMainSalary = round(firstForemanSalary + secondForemanSalary, 2)
        self.label_163.setText(str(summaryMainSalary))

        # Дополнительная зп
        additionalKf = self.doubleSpinBox_13.value() + self.doubleSpinBox_14.value()
        summaryAdditionalSalary = round(summaryMainSalary * additionalKf, 2)
        self.label_164.setText(str(summaryAdditionalSalary))

        # Отчисления на соц. нужды
        socialKf = self.doubleSpinBox_15.value() + self.doubleSpinBox_16.value() + self.doubleSpinBox_17.value() + self.doubleSpinBox_18.value()
        summarySocialSalary = round((summaryAdditionalSalary + summaryMainSalary) * socialKf, 2)
        self.label_165.setText(str(summarySocialSalary))

        # Затраты на материалы
        materialCost = float(self.label_2.text())
        self.label_166.setText(str(materialCost))

        # Затраты на машинное время
        machineHours = (self.timeEdit.time().minute() + 60 * self.timeEdit.time().hour()) * self.secondForemanDays / 60
        costPerMachineHour = self.doubleSpinBox_20.value()
        machineUsingKf = self.doubleSpinBox_21.value()
        machineHoursCost = round(machineHours * costPerMachineHour * machineUsingKf, 2)
        self.label_167.setText(str(machineHoursCost))

        # Накладные расходы
        overheadCost = round(summaryMainSalary * self.doubleSpinBox_19.value(), 2)
        self.label_168.setText(str(overheadCost))

        # Итог
        total = round(overheadCost + machineHoursCost + materialCost + summarySocialSalary + summaryAdditionalSalary + summaryMainSalary, 2)
        self.label_169.setText(str(total))
        self.label_171.setText(str(total) + ' руб.')

    def getSecondResult(self):
        # основное и вспом оборудование
        equipment = float(self.label_5.text())
        self.label_184.setText(str(round(equipment, 2)))

        # Строительство реконтрукция зданий помещений
        buildings = float(self.label_7.text())
        self.label_187.setText(str(round(buildings, 2)))

        # Приобретение типовых разработок пакетов
        packages = float(self.label_9.text())
        self.label_189.setText(str(round(packages, 2)))

        # Прокладка линий связи
        connectionLines = float(self.label_11.text())
        self.label_188.setText(str(round(connectionLines, 2)))

        # Создание информационной базы
        infoBase = float(self.label_13.text())
        self.label_190.setText(str(round(infoBase, 2)))

        # Подготовка и переподготовка кадров
        trainingStuff = float(self.label_23.text())
        self.label_191.setText(str(round(trainingStuff, 2)))

        # Итог
        total = round(equipment + buildings + packages + connectionLines + infoBase + trainingStuff, 2)
        self.label_192.setText(str(total))

    def get3Result(self):
        # основное и вспом оборудование
        equipment = float(self.label_25.text())
        self.label_203.setText(str(round(equipment, 2)))

        # Строительство реконтрукция зданий помещений
        buildings = float(self.label_41.text())
        self.label_206.setText(str(round(buildings, 2)))

        # Приобретение типовых разработок пакетов
        packages = float(self.label_43.text())
        self.label_208.setText(str(round(packages, 2)))

        # Прокладка линий связи
        connectionLines = float(self.label_47.text())
        self.label_207.setText(str(round(connectionLines, 2)))

        # Создание информационной базы
        infoBase = float(self.label_49.text())
        self.label_209.setText(str(round(infoBase, 2)))

        # Подготовка и переподготовка кадров
        trainingStuff = float(self.label_51.text())
        self.label_210.setText(str(round(trainingStuff, 2)))

        # Итог
        total = round(equipment + buildings + packages + connectionLines + infoBase + trainingStuff, 2)
        self.label_211.setText(str(total))

    def get4Result(self):
        # Проектирование и реализация проекта
        self.getFirstResult()
        self.getSecondResult()
        totalProject = round(float(self.label_192.text()) + float(self.label_169.text()), 2)
        self.label_29.setText(str(totalProject))

        # Реализация аналога
        totalAnalog = round(float(self.label_211.text()), 2)
        self.label_31.setText(str(totalAnalog))

    def get5Result(self):
        sumAnal = 0
        sumProj = 0

        powerProj = 0
        powerAnal = 0

        repairAnal = 0
        repairProj = 0

        materAnal = 0
        materProj = 0

        daysProj = 0
        for i in range(self.tableWidget_11.rowCount()):
            days = self.tableWidget_11.cellWidget(i, 2).value()
            daysProj += days

        daysAnal = 0
        for i in range(self.tableWidget_12.rowCount()):
            days = self.tableWidget_12.cellWidget(i, 2).value()
            daysAnal += days

        # anal
        for i in range(self.tableWidget_10.rowCount()):
            # амортизадница
            c = self.tableWidget_10.cellWidget(i, 4).value()
            a = self.doubleSpinBox_4.value()
            g = self.tableWidget_10.cellWidget(i, 1).value()
            t = daysAnal * round((self.tableWidget_10.cellWidget(i, 5).time().minute() + (self.tableWidget_10.cellWidget(i, 5).time().hour() * 60)) / 60, 2)
            f = self.spinBox.value() * round((self.timeEdit_2.time().minute() + self.timeEdit_2.time().hour() * 60) / 60, 2)

            sumAnal += (c * a * g * t) / f

            # силовая энергия
            n = self.tableWidget_10.cellWidget(i, 2).value()
            t = t
            g = self.tableWidget_10.cellWidget(i, 3).value()
            T = self.doubleSpinBox.value()

            powerAnal += n * t * g * T
            
            # затраты на ремонт
            Cp = self.doubleSpinBox_3.value()
            Cb = c
            t = t
            f = f

            repairAnal += (Cp * Cb * t) / f
            
            # затраты на материалы
            Cb = c

            materAnal += Cb * self.doubleSpinBox_24.value()

        nakladProj = round((sumProj + powerProj + repairProj + materProj + float(self.label_39.text())) * 0.2, 2)


        self.label_84.setText(self.label_39.text())
        self.label_56.setText(str(round(sumAnal, 2)))
        self.label_63.setText(str(round(powerAnal, 2)))
        self.label_69.setText(str(round(repairAnal, 2)))
        self.label_74.setText(str(round(materAnal, 2)))
        self.label_79.setText(str(round(nakladProj, 2)))
        
        itogAnal = float(self.label_39.text()) + round(sumAnal, 2) + round(powerAnal, 2) + round(repairAnal, 2) + round(materAnal, 2) + round(nakladProj, 2)

        self.label_91.setText(str(round(itogAnal, 2)))

        # proj
        for i in range(self.tableWidget_4.rowCount()):
            # амортизадница
            c = self.tableWidget_4.cellWidget(i, 4).value()
            a = self.doubleSpinBox_4.value()
            g = self.tableWidget_4.cellWidget(i, 1).value()
            t = daysProj * round((self.tableWidget_4.cellWidget(i, 5).time().minute() + (self.tableWidget_4.cellWidget(i, 5).time().hour() * 60)) / 60, 2)
            f = self.spinBox.value() * round((self.timeEdit_2.time().minute() + self.timeEdit_2.time().hour() * 60) / 60, 2)

            sumProj += (c * a * g * t) / f

            # силовая энергия
            n = self.tableWidget_4.cellWidget(i, 2).value()
            t = t
            g = self.tableWidget_4.cellWidget(i, 3).value()
            T = self.doubleSpinBox.value()

            powerProj += n * t * g * T

            # затраты на ремонт
            Cp = self.doubleSpinBox_3.value()
            Cb = c
            t = t
            f = f

            repairProj += (Cp * Cb * t) / f

            # затраты на материалы
            Cb = c

            materProj += Cb * self.doubleSpinBox_24.value()

        nakladProj = round((sumProj + powerProj + repairProj + materProj + float(self.label_36.text())) * self.doubleSpinBox_22.value(), 2)

        self.label_83.setText(self.label_36.text())
        self.label_57.setText(str(round(sumProj, 2)))
        self.label_62.setText(str(round(powerProj, 2)))
        self.label_68.setText(str(round(repairProj, 2)))
        self.label_73.setText(str(round(materProj, 2)))
        self.label_78.setText(str(round(nakladProj, 2)))

        itogProj = float(self.label_36.text()) + round(sumProj, 2) + round(powerProj, 2) + round(repairProj, 2) + round(materProj, 2) + round(nakladProj, 2)
        
        self.label_90.setText(str(round(itogProj, 2)))

    def get6Result(self):
        self.getFirstResult()
        self.getSecondResult()
        self.get3Result()
        self.get4Result()
        self.get5Result()

        Canal = self.label_91.text()
        self.label_98.setText(Canal)
        Cproj = self.label_90.text()
        self.label_115.setText(Cproj)

        Kanal = self.label_31.text()
        self.label_100.setText(Kanal)
        Kproj = self.label_29.text()
        self.label_113.setText(Kproj)

        a = float(self.label_20.text())

        e = self.doubleSpinBox_2.value()
        self.label_140.setText(str(e))

        Zanal = round(float(Canal) + e * float(Kanal), 2)
        self.label_102.setText(str(Zanal))
        Zproj = round(float(Cproj) + e * float(Kproj), 2)
        self.label_116.setText(str(Zproj))

        eff = round(Zanal * a - Zproj, 2)
        self.label_95.setText(str(eff))

        T = round(float(Kproj) / eff, 2) if eff != 0 else 0
        self.label_120.setText(str(T))

        Ef = round(1 / T, 2) if T != 0 else 0
        self.label_122.setText(str(Ef))

    def get7Result(self):
        self.getFirstResult()
        self.getSecondResult()
        self.get3Result()
        self.get4Result()
        self.get5Result()
        self.get6Result()

        # Затраты на разработку и внедрение проекта
        a = self.label_113.text()
        self.label_153.setText(a)

        # Общие эксплуатационные затраты, руб
        b = self.label_115.text()
        self.label_215.setText(b)

        # Экономический эффект, руб.:
        c = self.label_95.text()
        self.label_216.setText(c)

        # Коэффициент экономической эффективности:
        d = self.label_122.text()
        self.label_217.setText(d)

        # Срок окупаемости, лет
        e = self.label_120.text()
        self.label_218.setText(e)

        

    def toggleEf(self):
        if (self.pushButton_72.isChecked()):
            self.label_138.show()
            self.label_139.show()
            self.label_140.show()
        else:
            self.label_138.hide()
            self.label_139.hide()
            self.label_140.hide()

    def handleChangeSecondTable(self):
        dateFrom = self.tableWidget_2.cellWidget(1, 3).date().toPyDate()
        dateTo1 = dateFrom
        dateTo2 = dateFrom
        for i in range(0, self.rowCount):
            if (i in self.delimetrs):
                continue
            if (self.isEven):
                if (i == 1):
                    date = QtWidgets.QDateEdit()
                    date.setDate(dateFrom)
                    date.setDateRange(datetime.date.today(), datetime.date(3000, 12, 31))
                    date.dateChanged.connect(self.handleChangeSecondTable)
                    self.tableWidget_2.setCellWidget(i, 3, date)
                    dateTo = QtWidgets.QDateEdit()
                    dateTo.setDisabled(True)
                    days = int(self.tableWidget_2.cellWidget(i, 2).value()) - 1 if int(self.tableWidget_2.cellWidget(i, 2).value()) > 0 else 0
                    dateTo1 = dateFrom + datetime.timedelta(days = days)
                    dateTo.setDate(dateTo1)
                    self.tableWidget_2.setCellWidget(i, 4, dateTo)
                else:
                    date = QtWidgets.QDateEdit()
                    date.setDisabled(True)
                    date.setDate(dateFrom)
                    self.tableWidget_2.setCellWidget(i, 3, date)
                    dateTo = QtWidgets.QDateEdit()
                    dateTo.setDisabled(True)
                    days = int(self.tableWidget_2.cellWidget(i, 2).value()) - 1 if int(self.tableWidget_2.cellWidget(i, 2).value()) > 0 else 0
                    dateTo1 = dateFrom + datetime.timedelta(days = days)
                    dateTo.setDate(dateTo1)
                    self.tableWidget_2.setCellWidget(i, 4, dateTo)
            else:
                item = QtWidgets.QTableWidgetItem()
                item.setText(str("Программист"))
                self.tableWidget_2.setItem(i, 1, item)
                date = QtWidgets.QDateEdit()
                date.setDisabled(True)
                date.setDate(dateFrom)
                self.tableWidget_2.setCellWidget(i, 3, date)
                dateTo = QtWidgets.QDateEdit()
                dateTo.setDisabled(True)
                days = int(self.tableWidget_2.cellWidget(i, 2).value()) - 1 if int(self.tableWidget_2.cellWidget(i, 2).value()) > 0 else 0
                dateTo2 = dateFrom + datetime.timedelta(days = days)
                dateTo.setDate(dateTo2)
                self.tableWidget_2.setCellWidget(i, 4, dateTo)
            self.isEven = not self.isEven
            if (self.isEven):
                if (dateTo1 > dateTo2):
                    dateFrom = dateTo1 + datetime.timedelta(days = 1)
                else:
                    dateFrom = dateTo2 + datetime.timedelta(days = 1)
        finishDate = str(dateTo1 if dateTo1 > dateTo2 else dateTo2)
        date = finishDate.split("-")
        date = reversed(date)
        self.label_143.setText('.'.join(date))

    def addPK(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Добавить показатель качества',
            'Введите название показателя:')
        if ok:
            rowIndex = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowIndex)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(text))
            self.tableWidget.setItem(rowIndex, 0, item)

            item = QtWidgets.QDoubleSpinBox()
            item.setRange(0, 1)
            item.setSingleStep(0.01)
            item.setValue(0)            
            item.valueChanged.connect(self.handleChangeFirstTableValue)
            self.tableWidget.setCellWidget(rowIndex, 1, item)

            sum = 0
            for i in range(self.tableWidget.rowCount()):
                value = self.tableWidget.cellWidget(i, 1).value()
                sum += value
            if (sum >= 1):
                for i in range(self.tableWidget.rowCount()):
                    value = self.tableWidget.cellWidget(i, 1).value()
                    self.tableWidget.cellWidget(i, 1).setRange(0, value)

            item = QtWidgets.QComboBox()
            item.addItems(["1", "2", "3", "4", "5"])
            item.setCurrentIndex(2)
            item.currentIndexChanged.connect(self.handleChangeFirstTable)
            self.tableWidget.setCellWidget(rowIndex, 2, item)
            item = QtWidgets.QComboBox()
            item.addItems(["1", "2", "3", "4", "5"])
            item.setCurrentIndex(2)
            item.currentIndexChanged.connect(self.handleChangeFirstTable)
            self.tableWidget.setCellWidget(rowIndex, 3, item)

    def prevTab(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex() - 1)

    def nextTab(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex() + 1)

    def handleChangeTabIndex(self):
        if (self.tabWidget.currentIndex() == 7):
            self.getFirstResult()
        elif (self.tabWidget.currentIndex() == 20):
            self.getSecondResult()
        elif (self.tabWidget.currentIndex() == 21):
            self.get3Result()
        elif (self.tabWidget.currentIndex() == 22):
            self.get4Result()
        elif (self.tabWidget.currentIndex() == 25):
            self.get5Result()
        elif (self.tabWidget.currentIndex() == 26):
            self.get6Result()
        elif (self.tabWidget.currentIndex() == 27):
            self.get7Result()
 
    def toggleKTS(self):
        if (self.pushButton.isChecked()):
            self.label_21.show()
        else:
            self.label_21.hide()

    def handleChangeFirstTableValue(self):
        sum = 0
        for i in range(self.tableWidget.rowCount()):
            sum += self.tableWidget.cellWidget(i, 1).value()
        sum = round(sum, 2)
        if (sum >= 1):
            for i in range(self.tableWidget.rowCount()):
                value = self.tableWidget.cellWidget(i, 1).value()
                self.tableWidget.cellWidget(i, 1).setRange(0, value)
        else:
            for i in range(self.tableWidget.rowCount()):
                self.tableWidget.cellWidget(i, 1).setRange(0, 1)
        if (sum > 1):
            self.label_141.setStyleSheet("color: rgb(255, 0, 0)")
            self.label_141.setText('Сумма коэффициентов весомости: ' + str(sum) + ' Внимание! Так как сумма больше 1, вы можете получить неправильный результат.')
        elif (sum < 1):
            self.label_141.setStyleSheet("color: rgb(255, 0, 0)")
            self.label_141.setText('Сумма коэффициентов весомости: ' + str(sum) + ' Внимание! Так как сумма меньше 1, вы можете получить неправильный результат.')
        else: 
            self.label_141.setStyleSheet("color: rgb(0, 0, 0)")
            self.label_141.setText('Сумма коэффициентов весомости: ' + str(sum))

        self.handleChangeFirstTable()

    def handleChangeFirstTable(self):
        projX = 0
        analX = 0
        for i in range(self.tableWidget.rowCount()):
            projX += self.tableWidget.cellWidget(i, 1).value() * (self.tableWidget.cellWidget(i, 2).currentIndex() + 1)            
            analX += self.tableWidget.cellWidget(i, 1).value() * (self.tableWidget.cellWidget(i, 3).currentIndex() + 1) 
        projX = round(projX, 2)
        analX = round(analX, 2)
        self.label_16.setText(str(projX))          
        self.label_17.setText(str(analX))          
        self.label_20.setText(str(round(projX / analX, 2)))   

    def goToMenu(self):
        self.window = tea_welcome.MainUI()
        self.close()
        self.window.show()

def main():
    app = QtWidgets.QApplication([])
    application = DemoTeaUI()
    application.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()