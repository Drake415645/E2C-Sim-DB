from Utilities.utilities import *
from initTables import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QDir
from Utilities.utilities import createSchema, fromCSV, insertData, printTable, deleteTables
import workload as wl
from initTables import initTables
import sqlite3 as sq



db_path = CURR_PATH + '/Data/e2cDB.db'
conn = sq.connect(db_path)
cur = conn.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 779)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scen_label = QtWidgets.QLabel(self.centralwidget)
        self.scen_label.setGeometry(QtCore.QRect(480, 10, 91, 16))
        self.scen_label.setObjectName("scen_label")
        self.wl_label = QtWidgets.QLabel(self.centralwidget)
        self.wl_label.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.wl_label.setObjectName("wl_label")
        self.scen_load = QtWidgets.QPushButton(self.centralwidget)
        self.scen_load.setGeometry(QtCore.QRect(550, 700, 75, 23))
        self.scen_load.setObjectName("scen_load")
        self.wl_generate = QtWidgets.QPushButton(self.centralwidget)
        self.wl_generate.setGeometry(QtCore.QRect(650, 460, 75, 23))
        self.wl_generate.setObjectName("wl_generate")
        self.scen_path = QtWidgets.QLineEdit(self.centralwidget)
        self.scen_path.setGeometry(QtCore.QRect(630, 700, 61, 20))
        self.scen_path.setObjectName("scen_path")
        self.wl_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.wl_amount.setGeometry(QtCore.QRect(580, 430, 113, 20))
        self.wl_amount.setObjectName("wl_amount")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 461, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.update_label = QtWidgets.QLabel(self.centralwidget)
        self.update_label.setGeometry(QtCore.QRect(10, 530, 61, 16))
        self.update_label.setObjectName("update_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 500, 711, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.set_amt = QtWidgets.QLabel(self.centralwidget)
        self.set_amt.setGeometry(QtCore.QRect(490, 390, 131, 16))
        self.set_amt.setObjectName("set_amt")
        self.update_to = QtWidgets.QComboBox(self.centralwidget)
        self.update_to.setGeometry(QtCore.QRect(80, 530, 161, 22))
        self.update_to.setObjectName("update_to")
        self.update_to.addItem("")
        self.update_to.addItem("")
        self.update_to.addItem("")
        self.update_to.addItem("")
        self.fields = QtWidgets.QLineEdit(self.centralwidget)
        self.fields.setGeometry(QtCore.QRect(100, 570, 501, 20))
        self.fields.setObjectName("fields")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 570, 81, 16))
        self.label.setObjectName("label")
        self.update_submit = QtWidgets.QPushButton(self.centralwidget)
        self.update_submit.setGeometry(QtCore.QRect(610, 570, 75, 23))
        self.update_submit.setObjectName("update_submit")
        self.example_field = QtWidgets.QLineEdit(self.centralwidget)
        self.example_field.setGeometry(QtCore.QRect(100, 600, 501, 20))
        self.example_field.setObjectName("example_field")
        self.example = QtWidgets.QLabel(self.centralwidget)
        self.example.setGeometry(QtCore.QRect(30, 600, 51, 20))
        self.example.setObjectName("example")
        self.example_field.setDisabled(True)
        self.delete_id_label = QtWidgets.QLabel(self.centralwidget)
        self.delete_id_label.setGeometry(QtCore.QRect(20, 640, 71, 16))
        self.delete_id_label.setObjectName("delete_id_label")
        self.id_to_delete = QtWidgets.QLineEdit(self.centralwidget)
        self.id_to_delete.setGeometry(QtCore.QRect(90, 640, 61, 20))
        self.id_to_delete.setObjectName("id_to_delete")
        self.in_label = QtWidgets.QLabel(self.centralwidget)
        self.in_label.setGeometry(QtCore.QRect(60, 670, 21, 16))
        self.in_label.setObjectName("in_label")
        self.which_to_delete = QtWidgets.QComboBox(self.centralwidget)
        self.which_to_delete.setGeometry(QtCore.QRect(90, 670, 161, 22))
        self.which_to_delete.setObjectName("which_to_delete")
        self.which_to_delete.addItem("")
        self.which_to_delete.addItem("")
        self.which_to_delete.addItem("")
        self.delete_submit = QtWidgets.QPushButton(self.centralwidget)
        self.delete_submit.setGeometry(QtCore.QRect(90, 700, 75, 23))
        self.delete_submit.setObjectName("delete_submit")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 620, 711, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.num_tasks = QtWidgets.QLineEdit(self.centralwidget)
        self.num_tasks.setGeometry(QtCore.QRect(590, 90, 113, 20))
        self.num_tasks.setObjectName("num_tasks")
        self.starting_time = QtWidgets.QLineEdit(self.centralwidget)
        self.starting_time.setGeometry(QtCore.QRect(590, 130, 113, 20))
        self.starting_time.setObjectName("starting_time")
        self.ending_time = QtWidgets.QLineEdit(self.centralwidget)
        self.ending_time.setGeometry(QtCore.QRect(590, 170, 113, 20))
        self.ending_time.setObjectName("ending_time")
        self.scen_task_id = QtWidgets.QLineEdit(self.centralwidget)
        self.scen_task_id.setGeometry(QtCore.QRect(590, 50, 113, 20))
        self.scen_task_id.setObjectName("scen_task_id")
        self.scen_task_id_lbl = QtWidgets.QLabel(self.centralwidget)
        self.scen_task_id_lbl.setGeometry(QtCore.QRect(520, 50, 47, 13))
        self.scen_task_id_lbl.setObjectName("scen_task_id_lbl")
        self.num_tasks_lbl = QtWidgets.QLabel(self.centralwidget)
        self.num_tasks_lbl.setGeometry(QtCore.QRect(510, 90, 71, 16))
        self.num_tasks_lbl.setObjectName("num_tasks_lbl")
        self.starting_time_lbl = QtWidgets.QLabel(self.centralwidget)
        self.starting_time_lbl.setGeometry(QtCore.QRect(510, 130, 71, 16))
        self.starting_time_lbl.setObjectName("starting_time_lbl")
        self.ending_time_lbl = QtWidgets.QLabel(self.centralwidget)
        self.ending_time_lbl.setGeometry(QtCore.QRect(520, 170, 61, 16))
        self.ending_time_lbl.setObjectName("ending_time_lbl")
        self.add_scen_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_scen_btn.setGeometry(QtCore.QRect(650, 250, 75, 23))
        self.add_scen_btn.setObjectName("add_scen_btn")
        self.dist_scen_lbl = QtWidgets.QLabel(self.centralwidget)
        self.dist_scen_lbl.setGeometry(QtCore.QRect(520, 210, 61, 16))
        self.dist_scen_lbl.setObjectName("dist_scen_lbl")
        self.dist_combo = QtWidgets.QComboBox(self.centralwidget)
        self.dist_combo.setGeometry(QtCore.QRect(600, 210, 100, 22))
        self.dist_combo.setObjectName("dist_combo")
        self.dist_combo.addItem("")
        self.dist_combo.addItem("")
        self.dist_combo.addItem("")
        self.dist_combo.addItem("")
        self.pound_lbl = QtWidgets.QLabel(self.centralwidget)
        self.pound_lbl.setGeometry(QtCore.QRect(550, 430, 16, 16))
        self.pound_lbl.setObjectName("pound_lbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 21))
        self.menubar.setObjectName("menubar")
        self.menuE2C_Sim_Database_Demo = QtWidgets.QMenu(self.menubar)
        self.menuE2C_Sim_Database_Demo.setObjectName("menuE2C_Sim_Database_Demo")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuE2C_Sim_Database_Demo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.scen_load.clicked.connect(self.load_scen)
        self.wl_generate.clicked.connect(self.generate)
        self.update_to.currentTextChanged.connect(self.set_update_to)
        self.update_submit.clicked.connect(self.update_row)
        self.delete_submit.clicked.connect(self.delete)
        self.add_scen_btn.clicked.connect(self.add_scen)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.scen_label.setText(_translate("MainWindow", "Add a scenario"))
        self.wl_label.setText(_translate("MainWindow", "Generated Workload"))
        self.scen_load.setText(_translate("MainWindow", "Load(old)"))
        self.wl_generate.setText(_translate("MainWindow", "Generate"))
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
        self.scen_task_id_lbl.setText(_translate("MainWindow", "Task Id"))
        self.num_tasks_lbl.setText(_translate("MainWindow", "Num of Tasks"))
        self.starting_time_lbl.setText(_translate("MainWindow", "Starting time"))
        self.ending_time_lbl.setText(_translate("MainWindow", "Ending time"))
        self.add_scen_btn.setText(_translate("MainWindow", "Add Scenario"))
        self.dist_scen_lbl.setText(_translate("MainWindow", "Distribution"))
        self.dist_combo.setItemText(0, _translate("MainWindow", "1. Uniform"))
        self.dist_combo.setItemText(1, _translate("MainWindow", "2. Normal"))
        self.dist_combo.setItemText(2, _translate("MainWindow", "3. Exponential"))
        self.dist_combo.setItemText(3, _translate("MainWindow", "4. Spiked"))
        self.pound_lbl.setText(_translate("MainWindow", "#"))
        self.menuE2C_Sim_Database_Demo.setTitle(_translate("MainWindow", "E2C-Sim Database Demo"))


    def add_scen(self):
        scen_task_id = self.scen_task_id.text()
        starting_time = self.starting_time.text()
        ending_time = self.ending_time.text()
        num_tasks = self.num_tasks.text()
        dist = self.dist_combo.currentText()[0]
        
        data = (scen_task_id,starting_time,ending_time,num_tasks,dist)

        insertData(cur, conn, data, "scenario")
        printTable(cur,"scenario")
        

    def delete(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Are you sure you want to delete?")
        msgBox.setWindowTitle("Delete Row")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()

        if returnValue == QMessageBox.Ok:
            self.id = ""
            self.id_to_del = self.id_to_delete.text()
            self.table = self.which_to_delete.currentText()

            if(self.table == "machine_types"):
                self.id = "machine_id"
            if(self.table == "task_types"):
                self.id = "task_id"
            if(self.table == "distribution"):
                self.id = "dist_id"

            cur.execute(f"DELETE FROM {self.table} WHERE {self.id} = {self.id_to_del};")
            conn.commit()
            
            #above removes from db, this below shows to reflect live in the gui
            if(self.table == "task_types"):
                self.indexes = []
                self.amount = self.wl_amount.text()
                for k in range(int(self.amount)):
                    cur.execute(f"SELECT * FROM workload{k+1}")
                    self.length = len(cur.fetchall())

                    for i in range(self.length):
                        cur.execute(f"SELECT instance_id FROM workload{k+1} WHERE task_id = {self.id_to_del} AND instance_id = {i+1}")
                        self.del_task = cur.fetchone()
                        if self.del_task != None:
                            # print(str(k+1) + "--" + str(self.del_task[0])) 
                            self.indexes.append(self.del_task[0])
                            
                        self.indexes = sorted(self.indexes, reverse=True)
                    for idx in self.indexes:
                        # print(idx)
                        self.wk_table_list[k].removeRow(idx-1)
                    self.indexes.clear()

    def update_row(self):
        self.entry = self.fields.text().split(",")
        self.data = []
        
        if(self.update_to.currentText() == "machine_types"):
            self.machine_id = int(self.entry[0])
            self.machine_name = self.entry[1]
            self.no_of_replicas = int(self.entry[2])
            self.idle_power = float(self.entry[3])
            self.max_power = float(self.entry[4])
            self.num_of_cores = int(self.entry[5])
            self.cpu_clock = float(self.entry[6])
            self.memory = float(self.entry[7])

            cur.execute("INSERT INTO machine_types (machine_id,machine_name,no_of_replicas,idle_power,max_power,num_of_cores,cpu_clock,memory)"\
                        f"VALUES({self.machine_id},'{self.machine_name}',{self.no_of_replicas},{self.idle_power},{self.max_power},{self.num_of_cores},{self.cpu_clock},{self.memory})")
            conn.commit()
            # cur.execute("SELECT * FROM machine_types")
            # print(cur.fetchall())

            deleteTables(cur, conn, "eet")
            eet = """ CREATE TABLE IF NOT EXISTS eet (
            task_id INT NOT NULL,
            machine_id INT NOT NULL,
            expected_ex_time FLOAT NOT NULL,

            FOREIGN KEY (task_id) REFERENCES task_types(task_id),
            FOREIGN KEY (machine_id) REFERENCES machine_types(machine_id)
            ); """
            createSchema(cur, conn, eet)
                # --- eet ---
            # This table is derived from task_types and machine_types
            task_type_df = pd.read_sql_query(f'SELECT * FROM task_types', conn)
            machine_type_df = pd.read_sql_query(f'SELECT * FROM machine_types', conn)

            # Cartesian product of task_types and machine_types
            # (only using attributes we need)
            eet_list_buff = [
                (tt, mt) \
                for tt, _, _, _ in task_type_df.values.tolist() \
                for mt, _, _, _, _, _, _, _ in machine_type_df.values.tolist()
            ]

            # Insert randomized eet value for each tuple
            eet_list = []
            for entry in eet_list_buff:
                rnd = round(uniform(MIN_EX, MAX_EX), 2)
                eet_list.append(entry + (rnd, ))

            # Insert data to the eet table
            insertData(cur, conn, eet_list, 'eet')

        if(self.update_to.currentText() == "task_types"):
            self.task_id = int(self.entry[0])
            self.name = self.entry[1]
            self.detail = self.entry[2]
            self.urgency = self.entry[3]

            cur.execute(f"INSERT INTO task_types (task_id,name,detail,urgency)"\
            f"VALUES({self.task_id},'{self.name}','{self.detail}','{self.urgency}');")
            conn.commit()

            deleteTables(cur, conn, "eet")
            eet = """ CREATE TABLE IF NOT EXISTS eet (
            task_id INT NOT NULL,
            machine_id INT NOT NULL,
            expected_ex_time FLOAT NOT NULL,

            FOREIGN KEY (task_id) REFERENCES task_types(task_id),
            FOREIGN KEY (machine_id) REFERENCES machine_types(machine_id)
            ); """
            createSchema(cur, conn, eet)
                # --- eet ---
            # This table is derived from task_types and machine_types
            task_type_df = pd.read_sql_query(f'SELECT * FROM task_types', conn)
            machine_type_df = pd.read_sql_query(f'SELECT * FROM machine_types', conn)

            # Cartesian product of task_types and machine_types
            # (only using attributes we need)
            eet_list_buff = [
                (tt, mt) \
                for tt, _, _, _ in task_type_df.values.tolist() \
                for mt, _, _, _, _, _, _, _ in machine_type_df.values.tolist()
            ]

            # Insert randomized eet value for each tuple
            eet_list = []
            for entry in eet_list_buff:
                rnd = round(uniform(MIN_EX, MAX_EX), 2)
                eet_list.append(entry + (rnd, ))

            # Insert data to the eet table
            insertData(cur, conn, eet_list, 'eet')

        if(self.update_to.currentText() == "scenario"):
            self.task_id = int(self.entry[0])
            self.start_time = float(self.entry[1])
            self.end_time = float(self.entry[2])
            self.num_of_tasks = int(self.entry[3])
            self.dist_id = int(self.entry[4])

            cur.execute("INSERT INTO scenario (task_id,start_time,end_time,num_of_tasks,dist_id)"\
            f"VALUES({self.task_id},{self.start_time},{self.end_time},{self.num_of_tasks},{self.dist_id});")
            conn.commit()

        if(self.update_to.currentText() == "distribution"):
            self.dist_id = int(self.entry[0])
            self.name = self.entry[1]

            cur.execute("INSERT INTO distribution (dist_id,name)"\
            f"VALUES({self.dist_id},'{self.name}');")
            conn.commit()

    def set_update_to(self):
        if(self.update_to.currentText() == "machine_types"):
            self.example_field.setText("machine_id,machine_name,no_of_replicas,idle_power,max_power,num_of_cores,cpu_clock,memory")
        if(self.update_to.currentText() == "task_types"):
            self.example_field.setText("task_id,name,detail,urgency")
        if(self.update_to.currentText() == "scenario"):
            self.example_field.setText("task_id,start_time,end_time,num_of_tasks,dist_id")
        if(self.update_to.currentText() == "distribution"):
            self.example_field.setText("dist_id,name")
        

    def load_scen(self):
        self.path  = QFileDialog.getOpenFileName(None, caption='Choose Scenario File',
                                    directory=QDir.currentPath(),
                                    filter='*.csv')
        self.scen_path.setText(self.path[0])
        print(f'(main.py) {self.path[0]}')
        scen_values = fromCSV(self.path[0])
        # print(scen_values)
        cur.execute("DELETE FROM scenario;")
        print(scen_values)
        insertData(cur, conn, scen_values, 'scenario')
    
    def generate(self):
        self.amount = self.wl_amount.text()
        wl.createWorkload(cur, conn, int(self.amount))
        self.wk_table_list = []

        for k in range(int(self.amount)):
            self.tab = QtWidgets.QWidget()
            self.tab.setObjectName("tab")
            self.tab.layout = QtWidgets.QVBoxLayout()
            self.wk_table = QtWidgets.QTableWidget()
            self.wk_table.setColumnCount(4)
            self.tab.layout.addWidget(self.wk_table)
            self.tab.setLayout(self.tab.layout)

            item = QtWidgets.QTableWidgetItem("id")
            self.wk_table.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem("task type")
            self.wk_table.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem("task name")
            self.wk_table.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem("arrival")
            self.wk_table.setHorizontalHeaderItem(3, item)
            # item = QtWidgets.QTableWidgetItem("dist")
            # self.table.setHorizontalHeaderItem(4, item)
                
            cur.execute(f"SELECT * FROM workload{k+1}")
            self.length = len(cur.fetchall())
            self.wk_table.setRowCount(self.length)

            # printTable(cur, f"workload{k+1}")
            for i in range(self.length):
                cur.execute(f"SELECT task_id FROM workload{k+1} WHERE instance_id = {i+1}")
                self.task_id = cur.fetchone()
                cur.execute(f"SELECT name FROM workload{k+1} WHERE instance_id = {i+1}")
                self.name = cur.fetchone()
                cur.execute(f"SELECT arrival_time FROM workload{k+1} WHERE instance_id = {i+1}")
                self.arrival = cur.fetchone()
                # cur.execute(f"SELECT distribution.name FROM distribution, workload{k+1}, task_types WHERE workload.task_id = task_types.task_id, instance_id = {i+1}")
                # self.dist = cur.fetchone()

                self.wk_table.setItem(i,0, QtWidgets.QTableWidgetItem(str(i+1)))
                self.wk_table.setItem(i,1, QtWidgets.QTableWidgetItem(str(self.task_id)[1]))
                self.wk_table.setItem(i,2, QtWidgets.QTableWidgetItem(str(self.name)[2:4]))
                self.wk_table.setItem(i,3, QtWidgets.QTableWidgetItem(str(self.arrival)[1:-2]))
                # self.table.setItem(i,4, QtWidgets.QTableWidgetItem(str(self.dist)[1]))
                
            self.tabWidget.addTab(self.tab, f"WL{k+1}")
            self.wk_table_list.append(self.wk_table)
        


if __name__ == "__main__":
    import sys
    initTables(cur, conn)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())