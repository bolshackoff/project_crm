import psycopg2
conn = psycopg2.connect(dbname='crm', user='postgres', password='postegres', host='localhost')
cursor = conn.cursor()
name = input('Имя и Фамилия: ')
contact_number = int(input('Телефон +7'))
if 9000000000 > contact_number or contact_number > 9999999999:
    contact_number = int(input('Попробуйте еще раз. Телефон +7'))
email = input('email: ')
role = int(input('1)employee 2)manager: '))
while role !=1 and role != 2:
    int(input('Попробуйте еще раз. 1)employee 2)manager: '))
login = input('login: ')
def passwordcreate():
    password = input('password: ')
    password_rep = input('repeate password: ')
    if password != password_rep:
        print('Пароли не совпадают')
        passwordcreate()
    return password
password = passwordcreate()
cursor.execute('create user '+ login +'  with encrypted password %(password)s',{'password' : password})
conn.commit()
cursor.execute('grant connect on database crm to ' + login)
conn.commit()
cursor.execute('grant select on crm.schema_crm.\"products\" to ' + login)
conn.commit()
cursor.execute('grant select on crm.schema_crm.\"Reviews\" to ' + login)
conn.commit()
cursor.execute('grant create, usage on schema schema_crm to ' + login)
conn.commit()
if role == 1:
    cursor.execute('grant employee to ' + login)
    conn.commit()
    role = 'employee'
elif role == 2:
    cursor.execute('grant manager to ' + login)
    conn.commit()
    role = 'manager'
cursor.execute('insert into crm.schema_crm.\"EmployeesDATAccounts\" (login, password, email) values (%(login)s, md5(%(password)s), %(email)s)', {'login': login, 'password': password, 'email': email})
conn.commit()
cursor.execute('insert into crm.schema_crm.\"EmployeesDATATable\" (name, contact_number, email, role) values (%(name)s,'
               ' %(contact_number)s, %(email)s, %(role)s)', {'name': name, 'contact_number': contact_number,
                                                            'email': email, 'role': role})
conn.commit()

cursor.close()
conn.close()
