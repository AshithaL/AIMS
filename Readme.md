AIMS Project
===

 Accident & Incident Management application (AIMS) is 
 designed to help you manage accidents, incidents 
 and near misses. The system provides for a 
 structured investigation of accidents and 
 incidents, from which preventative actions 
 can then be generated and tracked. 

 Project Details
 ---
 
 There are several functionalities with respect to-
 
 **Admin** 
 
 **Supervisor** 
 
 **Worker** 
 
 Implementation
 ---
 
-> Python data structures.

-> [Sqlite3](https://www.tutorialspoint.com/sqlite/sqlite_python.htm) database for storage of records.
 
-> Database Connection
```
import sqlite3


con = sqlite3.connect('aims.db')
        print("Connection established: Database is created")
        return con

```

-> [Unit Testing](https://www.geeksforgeeks.org/unit-testing-python-unittest/) 
using [Mock and patch.](https://stackoverflow.com/questions/20536594/how-can-i-mock-sqlite3-cursor)
```
import unittest
from mock import patch



with patch('classname.sqlite3') as test:
test.connect().cursor().fetchall().return_value = ['aims.db']
X = bool(class.method())
assert(X, "Success")
```

