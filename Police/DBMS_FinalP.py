import sqlite3


def citizen_comp_register(NAME7, ID7, CID7, PLACE_OF_OCCURENCE7, DATE_OF_OCCURENCE7, DISTRICT7, SUBJECT7, DESCRIPTION7,
                          STATUS7):
    conn = sqlite3.connect(r'C:\Users\Pollam\Desktop\DBMS\dbms_final.db')
    c = conn.cursor()
    NAME = NAME7
    ID1 = ID7
    CID = CID7
    PLACE_OF_OCCURENCE = PLACE_OF_OCCURENCE7
    DATE_OF_OCCURENCE = DATE_OF_OCCURENCE7
    DISTRICT = DISTRICT7
    SUBJECT = SUBJECT7
    DESCRIPTION = DESCRIPTION7
    STATUS = STATUS7
    c.execute("insert into COMPLAINT values(?,?,?,?,?,?,?,?,?)",
              [NAME, ID1, CID, PLACE_OF_OCCURENCE, DATE_OF_OCCURENCE, DISTRICT, SUBJECT, DESCRIPTION, STATUS])
    print('pass')
    conn.commit()


def citizen_comp_status(CID):
    conn = sqlite3.connect(r'C:\Users\Pollam\Desktop\DBMS\dbms_final.db')
    c = conn.cursor()
    c.execute("select status from COMPLAINT where CID=(?)", [CID])
    rows = c.fetchall()

    for row in rows:
        for i in row:
            return i


def citizen_missing_view(DIS):
    conn = sqlite3.connect(r'C:\Users\Pollam\Desktop\DBMS\dbms_final.db')
    c = conn.cursor()
    c.execute("select * from MISSING where district=(?)", [DIS])
    rows = c.fetchall()
    for row in rows:
        print(row)
    print(13441241341)
    return rows


def citizen_missing_add(NAME6, CID6, DISTRICT6, HEIGHT6, COLOR6, CHARACTERISTICS6):
    conn = sqlite3.connect(r'C:\Users\Pollam\Desktop\DBMS\dbms_final.db')
    c = conn.cursor()
    NAME = NAME6
    CID1 = CID6
    DISTRICT = DISTRICT6
    HEIGHT = HEIGHT6
    COLOR = COLOR6
    CHARACTERISTICS = CHARACTERISTICS6

    c.execute("insert into missing values(?,?,?,?,?,?)", [NAME, CID1, DISTRICT, HEIGHT, COLOR, CHARACTERISTICS])
    c.execute("select * from missing")
    rows = c.fetchall()
    for row in rows:
        print(row)

    conn.commit()


def citizen_criminal_area(dis):
    conn = sqlite3.connect(r'C:\Users\Pollam\Desktop\DBMS\dbms_final.db')
    c = conn.cursor()
    c.execute("select * from CRIMINALS where district=(?)", [dis])
    rows = c.fetchall()

    for row in rows:
        print(row)
    return rows
    conn.commit()


def citizen_police_details(DISTRICT):
    conn = sqlite3.connect(r'C:\Users\Pollam\Desktop\DBMS\dbms_final.db')
    c = conn.cursor()
    c.execute("select * from POLICE where DISTRICT=(?)", [DISTRICT])
    rows = c.fetchall()

    for row in rows:
        print(row)
    return rows


def police_signup(NAME0, PID0, GENDER0, DATE_OF_BIRTH0, DISTRICT0, ADDRESS0, DESIGNATION0,sal,ms):
    conn = sqlite3.connect(r'C:\Users\Pollam\Desktop\DBMS\dbms_final.db')
    c = conn.cursor()
    NAME = NAME0
    PID = PID0
    GENDER = GENDER0
    DATE_OF_BIRTH = DATE_OF_BIRTH0
    DISTRICT = DISTRICT0
    ADDRESS = ADDRESS0
    DESIGNATION = DESIGNATION0
    salary=sal
    marital_status=ms
    c.execute("insert into POLICE values(?,?,?,?,?,?,?,?,?)",
              [NAME, PID, GENDER, DATE_OF_BIRTH, DISTRICT, ADDRESS, DESIGNATION,salary,marital_status])
    conn.commit()
    from . import FR
    FR.trainer(PID)


def police_signin_COMP(DIS):
    conn = sqlite3.connect(r'C:\Users\Pollam\Desktop\DBMS\dbms_final.db')
    c = conn.cursor()
    c.execute("select *  from COMPLAINT where district=(?)", [DIS])
    rows = c.fetchall()

    for row in rows:
        print(row)
    conn.commit()
    return rows

def police_signin_enter_crim(NAME9, CRIMINAL_ID9, GENDER9, DISTRICT9, ACCUSED_FOR9, HEIGHT9, COLOR9):
    conn = sqlite3.connect(r'C:\Users\Pollam\Desktop\DBMS\dbms_final.db')
    c = conn.cursor()
    NAME = NAME9
    CRIMINAL_ID = CRIMINAL_ID9
    GENDER = GENDER9
    DISTRICT = DISTRICT9
    ACCUSED_FOR = ACCUSED_FOR9
    HEIGHT = HEIGHT9
    COLOR = COLOR9

    c.execute("insert into CRIMINALS values(?,?,?,?,?,?,?)",[NAME, CRIMINAL_ID, GENDER, DISTRICT, ACCUSED_FOR, HEIGHT, COLOR])
    print(1234)
    conn.commit()


def police_signin_missperson(CID1):
    conn = sqlite3.connect('dbms_final.db')
    c = conn.cursor()
    c.execute("select * from MISSING where CID1=(?)", [CID1])
    rows = c.fetchall()

    for row in rows:
        print(row)
    conn.commit()


def police_signin_citizen(dis):
    conn = sqlite3.connect(r'C:\Users\Pollam\Desktop\DBMS\dbms_final.db')
    c = conn.cursor()
    c.execute("select * from CITIZEN where district=(?)", [dis])
    rows = c.fetchall()

    return rows



conn = sqlite3.connect(r'C:\Users\Pollam\Desktop\DBMS\dbms_final.db')
c = conn.cursor()
# c.execute("create table missing(name varchar2(20),id varchar2(10) PRIMARY KEY,district varchar2(10),height varchar2(10),color varchar2(10),characteristics varchar2(40))")
# c.execute("insert into missing values('Gowtham','1234','hyderabad','140','fair','tall')")
DIS='Hyderabad'
c.execute("select *  from criminals")
rows = c.fetchall()
for row in rows:
    print(row)
#conn.commit()
print(2314)

conn.commit()
