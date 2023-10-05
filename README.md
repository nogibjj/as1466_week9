# IDS706-Week5-project

[![Python CI](https://github.com/Nastiiasaenko/IDS706-Week1-project/actions/workflows/main.yml/badge.svg)](https://github.com/Nastiiasaenko/IDS706-Week1-project/actions/workflows/main.yml)

This project uses main.py file to connect to LifeDB.db database and utilized mylib functions to update, read, create a table in the db, query and drop the table. The repo consists of: 

* Devcontainer with DockerFile
* workflows with github actions
* gitingnore file
* this Readme.md file
* requirements.txt file
* **main.py file  that can be used in the terminal as a command-line tool.**

  Outline of the project:
  In  mylib:
  1) extract.py - extract dataset by a URL and extract it into a github folder
  2) transform_load.py - transforms the dataset and loads it into the dataset
  3) query.py - connects to the database and allows to perform queries on the database.
  4) crud.py - contains functions to perform crud operations on the database.
 
  #### Here's the connection to the database that happens in the functions
  ![image](https://github.com/nogibjj/as1466_sqlite_lab/assets/54864655/18c478c5-6fd5-46e0-b13e-d7c54dfaef31)

  ### Two SQL queries on the database
  1) 
 
![image](https://github.com/nogibjj/as1466_sqlite_lab/assets/54864655/c93fa827-6f13-438b-8c19-1abf987c8687)

2) ![image](https://github.com/nogibjj/as1466_sqlite_lab/assets/54864655/3bbda405-3217-4436-9dd8-b09be97fbe52)

#### Crud Operations 
![image](https://github.com/nogibjj/as1466_sqlite_lab/assets/54864655/8f0c72e5-d27b-4483-aaff-7b80dfeb2189)
![image](https://github.com/nogibjj/as1466_sqlite_lab/assets/54864655/b973e53c-8c9e-49bb-844e-b5bc8bd06922)
![image](https://github.com/nogibjj/as1466_sqlite_lab/assets/54864655/4ba58465-9b2f-41df-8f58-48da9534eecf)
![image](https://github.com/nogibjj/as1466_sqlite_lab/assets/54864655/ffc4ecec-1f9c-40c0-b0b4-bdd99b659224)



