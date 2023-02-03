#just in case i need these again in future
    # self.update_to.currentTextChanged.connect(self.set_update_to)


#  def update_row(self):
        # self.entry = self.fields.text().split(",")
        # self.data = []
        
        # if(self.update_to.currentText() == "machine_types"):
        #     self.machine_id = int(self.entry[0])
        #     self.machine_name = self.entry[1]
        #     self.no_of_replicas = int(self.entry[2])
        #     self.idle_power = float(self.entry[3])
        #     self.max_power = float(self.entry[4])
        #     self.num_of_cores = int(self.entry[5])
        #     self.cpu_clock = float(self.entry[6])
        #     self.memory = float(self.entry[7])

        #     cur.execute("INSERT INTO machine_types (machine_id,machine_name,no_of_replicas,idle_power,max_power,num_of_cores,cpu_clock,memory)"\
        #                 f"VALUES({self.machine_id},'{self.machine_name}',{self.no_of_replicas},{self.idle_power},{self.max_power},{self.num_of_cores},{self.cpu_clock},{self.memory})")
        #     conn.commit()
        #     # cur.execute("SELECT * FROM machine_types")
        #     # print(cur.fetchall())

        #     deleteTables(cur, conn, "eet")
        #     eet = """ CREATE TABLE IF NOT EXISTS eet (
        #     task_id INT NOT NULL,
        #     machine_id INT NOT NULL,
        #     expected_ex_time FLOAT NOT NULL,

        #     FOREIGN KEY (task_id) REFERENCES task_types(task_id),
        #     FOREIGN KEY (machine_id) REFERENCES machine_types(machine_id)
        #     ); """
        #     createSchema(cur, conn, eet)
        #         # --- eet ---
        #     # This table is derived from task_types and machine_types
        #     task_type_df = pd.read_sql_query(f'SELECT * FROM task_types', conn)
        #     machine_type_df = pd.read_sql_query(f'SELECT * FROM machine_types', conn)

        #     # Cartesian product of task_types and machine_types
        #     # (only using attributes we need)
        #     eet_list_buff = [
        #         (tt, mt) \
        #         for tt, _, _, _ in task_type_df.values.tolist() \
        #         for mt, _, _, _, _, _, _, _ in machine_type_df.values.tolist()
        #     ]

        #     # Insert randomized eet value for each tuple
        #     eet_list = []
        #     for entry in eet_list_buff:
        #         rnd = round(uniform(MIN_EX, MAX_EX), 2)
        #         eet_list.append(entry + (rnd, ))

        #     # Insert data to the eet table
        #     insertData(cur, conn, eet_list, 'eet')

        # if(self.update_to.currentText() == "task_types"):
        #     self.task_id = int(self.task_id.text())
        #     self.name = self.task_name.text()
        #     self.detail = self.detail.text()
        #     self.urgency = self.urgency.text()

        #     cur.execute(f"INSERT INTO task_types (task_id,name,detail,urgency)"\
        #     f"VALUES({self.task_id},'{self.name}','{self.detail}','{self.urgency}');")
        #     conn.commit()

        #     deleteTables(cur, conn, "eet")
        #     eet = """ CREATE TABLE IF NOT EXISTS eet (
        #     task_id INT NOT NULL,
        #     machine_id INT NOT NULL,
        #     expected_ex_time FLOAT NOT NULL,

        #     FOREIGN KEY (task_id) REFERENCES task_types(task_id),
        #     FOREIGN KEY (machine_id) REFERENCES machine_types(machine_id)
        #     ); """
        #     createSchema(cur, conn, eet)
        #         # --- eet ---
        #     # This table is derived from task_types and machine_types
        #     task_type_df = pd.read_sql_query(f'SELECT * FROM task_types', conn)
        #     machine_type_df = pd.read_sql_query(f'SELECT * FROM machine_types', conn)

        #     # Cartesian product of task_types and machine_types
        #     # (only using attributes we need)
        #     eet_list_buff = [
        #         (tt, mt) \
        #         for tt, _, _, _ in task_type_df.values.tolist() \
        #         for mt, _, _, _, _, _, _, _ in machine_type_df.values.tolist()
        #     ]

        #     # Insert randomized eet value for each tuple
        #     eet_list = []
        #     for entry in eet_list_buff:
        #         rnd = round(uniform(MIN_EX, MAX_EX), 2)
        #         eet_list.append(entry + (rnd, ))

        #     # Insert data to the eet table
        #     insertData(cur, conn, eet_list, 'eet')

        # if(self.update_to.currentText() == "scenario"):
        #     self.task_id = int(self.entry[0])
        #     self.start_time = float(self.entry[1])
        #     self.end_time = float(self.entry[2])
        #     self.num_of_tasks = int(self.entry[3])
        #     self.dist_id = int(self.entry[4])

        #     cur.execute("INSERT INTO scenario (task_id,start_time,end_time,num_of_tasks,dist_id)"\
        #     f"VALUES({self.task_id},{self.start_time},{self.end_time},{self.num_of_tasks},{self.dist_id});")
        #     conn.commit()

        # if(self.update_to.currentText() == "distribution"):
        #     self.dist_id = int(self.entry[0])
        #     self.name = self.entry[1]

        #     cur.execute("INSERT INTO distribution (dist_id,name)"\
        #     f"VALUES({self.dist_id},'{self.name}');")
        #     conn.commit()

    # def set_update_to(self):
    #     if(self.update_to.currentText() == "machine_types"):
    #         self.example_field.setText("machine_id,machine_name,no_of_replicas,idle_power,max_power,num_of_cores,cpu_clock,memory")
    #     if(self.update_to.currentText() == "task_types"):
    #         self.example_field.setText("task_id,name,detail,urgency")
    #     if(self.update_to.currentText() == "scenario"):
    #         self.example_field.setText("task_id,start_time,end_time,num_of_tasks,dist_id")
    #     if(self.update_to.currentText() == "distribution"):
    #         self.example_field.setText("dist_id,name")
        