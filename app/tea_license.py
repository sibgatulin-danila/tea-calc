from PyQt5 import QtWidgets
import datetime
import sys
 
# Импортируем наш шаблон.
from viewsPy.tea_license import Ui_mainWindow as tea_license
import main as tea_welcome
 
class TeaLicenseUI(QtWidgets.QMainWindow, tea_license):
    def __init__(self):
        super(TeaLicenseUI, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.goMainWindow)

    def goMainWindow(self):
        self.mainWindow = tea_welcome.MainUI()
        # self.mainWindow.show()
        self.close()

def main():
    app = QtWidgets.QApplication([])
    application = TeaLicenseUI()
    application.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()