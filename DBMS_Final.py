import sqlite3

def citizen_comp_register(NAME7,ID7,CID7,PLACE_OF_OCCURENCE7,DATE_OF_OCCURENCE7,DISTRICT7,SUBJECT7,DESCRIPTION7,STATUS7):
    conn = sqlite3.connect('dbms_final.db')
    c=conn.cursor()
    NAME=NAME7
    PID1=PID7
    CID=CID7
    PLACE_OF_OCCURENCE=PLACE_OF_OCCURENCE7
    DATE_OF_OCCURENCE=DATE_OF_OCCURENCE7
    DISTRICT=DISTRICT7
    SUBJECT=SUBJECT7
    DESCRIPTION=DESCRIPTION7
    STATUS=STATUS7
    c.execute("insert into COMPLAINT values(?,?,?,?,?,?,?,?,?)" ,[NAME,ID1,CID,PLACE_OF_OCCURENCE,DATE_OF_OCCURENCE,DISTRICT,SUBJECT,DESCRIPTION,STATUS])
    print('pass')
    conn.commit()

def citizen_comp_status(CID):
    conn = sqlite3.connect('dbms_final.db')
    c = conn.cursor()
    c.execute("select * from COMPLAINT where CID=?",CID)
    rows=c.fetchall()

    for row in rows:
        print(row)
    conn.commit()
def citizen_missing_view(CID):
    conn = sqlite3.connect('dbms_final.db')
    c = conn.cursor()
    c.execute("select * from MISSING where CID=?",CID)
    rows=c.fetchall()

    for row in rows:
        print(row)
    conn.commit()
def citizen_missing_add(NAME6,CID6,DISTRICT6,HEIGHT6,COLOR6,CHARACTERISTICS6):
    conn = sqlite3.connect('dbms_final.db')
    c = conn.cursor()
    NAME=NAME6
    CID1=CID6
    DISTRICT=DISTRICT6
    HEIGHT=HEIGHT6
    COLOR=COLOR6
    CHARACTERISTICS=CHARACTERISTICS6
    
    c.execute("insert into MISSING values(?,?,?,?,?,?)",[NAME,CID1,DISTRICT,HEIGHT,COLOR,CHARACTERISTICS])
    conn.commit()
def citizen_criminal_area(CRIMINAL_ID):
    conn = sqlite3.connect('dbms_final.db')
    c = conn.cursor()
    c.execute("select * from CRIMINALS where CRIMINAL_ID=?",CRIMINAL_ID)
    rows=c.fetchall()

    for row in rows:
        print(row)
    conn.commit()
def citizen_police_details(DISTRICT):
    conn = sqlite3.connect('dbms_final.db')
    c = conn.cursor()
    c.execute("select * from POLICE where DISTRICT=?",DISTRICT)
    rows=c.fetchall()

    for row in rows:
        print(row)

    conn.commit()

def  police_signup(NAME0,PID0,GENDER0,DATE_OF_BIRTH0,DISTRICT0,ADDRESS0,DESIGNATION0):
    conn = sqlite3.connect('dbms_final.db')
    c = conn.cursor()
    NAME=NAME0
    PID=PID0
    GENDER=GENDER0
    DATE_OF_BIRTH=DATE_OF_BIRTH0
    DISTRICT=DISTRICT0
    ADDRESS=ADDRESS0
    DESIGNATION=DESIGNATION0
    
    c.execute("insert into POLICE values(?,?,?,?,?,?,?)" ,[NAME,PID,GENDER,DATE_OF_BIRTH,DISTRICT,ADDRESS,DESIGNATION])
    conn.commit()
def police_signin_COMP(CID):
    conn = sqlite3.connect('dbms_final.db')
    c = conn.cursor()
    c.execute("select * from COMPLAINT where CID=?",CID)
    rows=c.fetchall()

    for row in rows:
        print(row)
    conn.commit()
def police_signin_enter_crim(NAME9,CRIMINAL_ID9,GENDER9,DISTRICT9,ACCUSED_FOR9,HEIGHT9,COLOR9):
    conn = sqlite3.connect('dbms_final.db')
    c = conn.cursor()
    NAME=NAME9
    CRIMINAL_ID=CRIMINAL_ID9
    GENDER=GENDER9
    DISTRICT=DISTRICT9
    ACCUSED_FOR=ACCUSED_FOR9
    HEIGHT=HEIGHT9
    COLOR=COLOR9
    
    c.execute("insert into CRIMINALS values(?,?,?,?,?,?,?)" ,[NAME,CRIMINAL_ID,GENDER,DISTRICT,ACCUSED_FOR,HEIGHT,COLOR])

    conn.commit()
def police_signin_missperson(CID1):
    conn = sqlite3.connect('dbms_final.db')
    c = conn.cursor()
    c.execute("select * from MISSING where CID1=?",[CID1])
    rows=c.fetchall()

    for row in rows:
        print(row)
    conn.commit()
def police_signin_citizen(CID):
    conn = sqlite3.connect('dbms_final.db')
    c = conn.cursor()
    c.execute("select * from CITIZEN where CID=?",CID)
    rows=list(c.fetchall())

    for row in rows:
        print(row)
    conn.commit()
def district_select():
    conn = sqlite3.connect('dbms_final.db')
    c = conn.cursor()
    c.execute("select DISTRICT_NAME from DISTRICT")
    conn.commit()


