# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E2C-Sim-DbDebug.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(729, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scen_label = QtWidgets.QLabel(self.centralwidget)
        self.scen_label.setGeometry(QtCore.QRect(490, 60, 91, 16))
        self.scen_label.setObjectName("scen_label")
        self.scen_submit = QtWidgets.QPushButton(self.centralwidget)
        self.scen_submit.setGeometry(QtCore.QRect(580, 120, 75, 23))
        self.scen_submit.setObjectName("scen_submit")
        self.wl_label = QtWidgets.QLabel(self.centralwidget)
        self.wl_label.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.wl_label.setObjectName("wl_label")
        self.scen_load = QtWidgets.QPushButton(self.centralwidget)
        self.scen_load.setGeometry(QtCore.QRect(490, 120, 75, 23))
        self.scen_load.setObjectName("scen_load")
        self.wl_generate = QtWidgets.QPushButton(self.centralwidget)
        self.wl_generate.setGeometry(QtCore.QRect(490, 210, 75, 23))
        self.wl_generate.setObjectName("wl_generate")
        self.scen_path = QtWidgets.QLineEdit(self.centralwidget)
        self.scen_path.setGeometry(QtCore.QRect(490, 90, 221, 20))
        self.scen_path.setObjectName("scen_path")
        self.wl_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.wl_amount.setGeometry(QtCore.QRect(490, 180, 113, 20))
        self.wl_amount.setObjectName("wl_amount")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 461, 201))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.update_label = QtWidgets.QLabel(self.centralwidget)
        self.update_label.setGeometry(QtCore.QRect(10, 280, 61, 16))
        self.update_label.setObjectName("update_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 250, 711, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.set_amt = QtWidgets.QLabel(self.centralwidget)
        self.set_amt.setGeometry(QtCore.QRect(490, 160, 131, 16))
        self.set_amt.setObjectName("set_amt")
        self.update_to = QtWidgets.QComboBox(self.centralwidget)
        self.update_to.setGeometry(QtCore.QRect(80, 280, 161, 22))
        self.update_to.setObjectName("update_to")
        self.update_to.addItem("")
        self.update_to.addItem("")
        self.update_to.addItem("")
        self.update_to.addItem("")
        self.fields = QtWidgets.QLineEdit(self.centralwidget)
        self.fields.setGeometry(QtCore.QRect(100, 320, 501, 20))
        self.fields.setObjectName("fields")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 320, 81, 16))
        self.label.setObjectName("label")
        self.update_submit = QtWidgets.QPushButton(self.centralwidget)
        self.update_submit.setGeometry(QtCore.QRect(610, 320, 75, 23))
        self.update_submit.setObjectName("update_submit")
        self.example_field = QtWidgets.QLineEdit(self.centralwidget)
        self.example_field.setGeometry(QtCore.QRect(100, 350, 501, 20))
        self.example_field.setObjectName("example_field")
        self.example = QtWidgets.QLabel(self.centralwidget)
        self.example.setGeometry(QtCore.QRect(30, 350, 51, 20))
        self.example.setObjectName("example")
        self.delete_id_label = QtWidgets.QLabel(self.centralwidget)
        self.delete_id_label.setGeometry(QtCore.QRect(20, 440, 71, 16))
        self.delete_id_label.setObjectName("delete_id_label")
        self.id_to_delete = QtWidgets.QLineEdit(self.centralwidget)
        self.id_to_delete.setGeometry(QtCore.QRect(90, 440, 61, 20))
        self.id_to_delete.setObjectName("id_to_delete")
        self.in_label = QtWidgets.QLabel(self.centralwidget)
        self.in_label.setGeometry(QtCore.QRect(60, 470, 21, 16))
        self.in_label.setObjectName("in_label")
        self.which_to_delete = QtWidgets.QComboBox(self.centralwidget)
        self.which_to_delete.setGeometry(QtCore.QRect(90, 470, 161, 22))
        self.which_to_delete.setObjectName("which_to_delete")
        self.which_to_delete.addItem("")
        self.which_to_delete.addItem("")
        self.which_to_delete.addItem("")
        self.delete_submit = QtWidgets.QPushButton(self.centralwidget)
        self.delete_submit.setGeometry(QtCore.QRect(90, 500, 75, 23))
        self.delete_submit.setObjectName("delete_submit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 729, 21))
        self.menubar.setObjectName("menubar")
        self.menuE2C_Sim_Database_Demo = QtWidgets.QMenu(self.menubar)
        self.menuE2C_Sim_Database_Demo.setObjectName("menuE2C_Sim_Database_Demo")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuE2C_Sim_Database_Demo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.scen_label.setText(_translate("MainWindow", "Select Scenario(s)"))
        self.scen_submit.setText(_translate("MainWindow", "Submit"))
        self.wl_label.setText(_translate("MainWindow", "Generated Workload"))
        self.scen_load.setText(_translate("MainWindow", "Load"))
        self.wl_generate.setText(_translate("MainWindow", "Generate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.update_label.setText(_translate("MainWindow", "Add row to:"))
        self.set_amt.setText(_translate("MainWindow", "Set Amount of Workloads"))
        self.update_to.setItemText(0, _translate("MainWindow", "machine_types"))
        self.update_to.setItemText(1, _translate("MainWindow", "task_types"))
        self.update_to.setItemText(2, _translate("MainWindow", "scenario"))
        self.update_to.setItemText(3, _translate("MainWindow", "distribution"))
        self.label.setText(_translate("MainWindow", "Enter each field:"))
        self.update_submit.setText(_translate("MainWindow", "Submit"))
        self.example.setText(_translate("MainWindow", "(example):"))
        self.delete_id_label.setText(_translate("MainWindow", "Delete Id of:"))
        self.in_label.setText(_translate("MainWindow", "In:"))
        self.which_to_delete.setItemText(0, _translate("MainWindow", "machine_types"))
        self.which_to_delete.setItemText(1, _translate("MainWindow", "task_types"))
        self.which_to_delete.setItemText(2, _translate("MainWindow", "distribution"))
        self.delete_submit.setText(_translate("MainWindow", "Delete"))
        self.menuE2C_Sim_Database_Demo.setTitle(_translate("MainWindow", "E2C-Sim Database Demo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())