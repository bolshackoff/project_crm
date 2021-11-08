import psycopg2
import random

conn = psycopg2.connect(dbname='crm', user='postgres', password='postgres', host='localhost')
cursor = conn.cursor()

def randName():
    # for i in range():
    rand_id_name = random.randint(19903, 71431)
    rand_id_surname = random.randint(1, 22284)
    cursor.execute("select name, sex from crm.names.russian_names where id = %s", (rand_id_name,))
    tample = cursor.fetchall()[0]
    name = tample[0]
    sex_name = tample[1]
    cursor.execute("select surname from crm.names.russian_surnames where id = %s", (rand_id_surname,))
    surname = cursor.fetchone()[0]
    print(surname)
    if (surname.endswith('ова') or surname.endswith('ева') or surname.endswith('ина')) and sex_name == 'Ж' or (surname.endswith('ов') or surname.endswith('ев') or surname.endswith('ин')) and sex_name == 'М':
        full_name = name + ' ' + surname
        print((full_name))
        return full_name
    elif (not(surname.endswith('ов') or surname.endswith('ев') or surname.endswith('ин') or surname.endswith('ова') or surname.endswith('ева') or surname.endswith('ина')) and name != None and surname != None):
        full_name = name + ' ' + surname
        print(full_name)
        return full_name
    else:
       return randName()


def randEmail():
    login_length = random.randint(3, 13)
    login = ''
    for i in range(login_length):
        if random.choice([True, False]):
            login += chr(random.randint(90 - 25, 90))
        else:
            login += chr(random.randint(97, 122))
    domen_length = random.randint(3, 13)
    domen = ''
    for i in range(domen_length):
        if random.choice([True, False]):
            domen += chr(random.randint(90 - 25, 90))
        else:
            domen += chr(random.randint(97, 122))
    email = login + '@' + domen + '.com'
    return email

def randNumbers():
     return '+7' + str(random.randint(9000000001, 9999999999))

def randRole():
    return random.choices(['manager', 'employee'], weights=[10, 90])

def randFace():
    return random.choices(['entity', 'natural'], weights=[50, 50])

def randClient():
    return random.choices(['potentional', 'current'], weights=[20, 80])

for i in range(int(input("Количество работников "))):
    cursor.execute('insert into crm.schema_crm.\"EmployeesDATATable\" (name, contact_number, email, role) values (%(name)s, %(numbers)s, %(email)s, %(role)s)', {'name' : randName(), 'email' : randEmail(), 'numbers' : randNumbers(), 'role' : randRole()})
    conn.commit()

for i in range(int(input("Количество клиентов "))):
    cursor.execute('insert into crm.schema_crm.\"ClientsDATATable\" (name, contact_number, email, face, client) values (%(name)s, %(contact_numbers)s, %(email)s, %(face)s, %(client)s)', {'name': randName(), 'contact_numbers': randNumbers(), 'email': randEmail(), 'face': randFace(), 'client': randClient()})
    conn.commit()

cursor.close()
conn.close()
