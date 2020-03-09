from PyQt5 import QtWidgets
import datetime
import sys, os
 
from viewsPy.main import Ui_MainWindow as tea_welcome
import tea
import demo_tea
import tea_license
 
class MainUI(QtWidgets.QMainWindow, tea_welcome):
    def __init__(self):
        super(MainUI, self).__init__()
        self.setupUi(self)

        self.action_3.setCheckable(True)
        self.action_3.toggled.connect(self.isShowProgrammers)
        self.action.triggered.connect(self.showDocument)
        self.pushButton.clicked.connect(self.startTea)
        self.pushButton_3.clicked.connect(self.startDemoTea)

        self.action_4.triggered.connect(self.startLicenseWindow)

        self.label.hide()

    def startLicenseWindow(self):
        self.window = tea_license.TeaLicenseUI()
        self.window.show()
        # self.close()

    def showDocument(self):
        # app_dir = sys.path[0] or os.path.dirname(os.path.realpath(sys.argv[0])) or os.getcwd()
        app_dir = os.path.abspath(__file__)
        os.system(os.path.join("file.pdf"))

    def isShowProgrammers(self):
        if (self.action_3.isChecked()):
            self.label.show()
        else:
            self.label.hide()

    def startDemoTea(self):
        self.window = demo_tea.DemoTeaUI()
        self.window.show()
        self.close()

    def startTea(self):
        self.window = tea.TeaUI()
        self.window.show()
        self.close()

def main():
    app = QtWidgets.QApplication([])
    application = MainUI()
    application.show()
    
    sys.exit(app.exec())
 
if __name__ == '__main__':
    main()