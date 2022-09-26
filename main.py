import psycopg2
from datetime import datetime
import getpass
def printtable(table):
    print()
    print("{:^3}".format('id'), "{:^25}".format('client_name'), "{:^14}".format('contact_number'),
          "{:^30}".format('description'), "{:^30}".format('address'), "{:^25}".format('author_name'),
          "{:^25}".format('executor_name'), "{:^8}".format('in_work'),
          "{:^10}".format('creates'), "{:^10}".format('completed'), "{:^5}".format('code_of_product'), sep='|')
    def _():
        for i in range(194):
            print('-', end='')
        print()
    array = []
    for i in table:
        array.append(i)

    for i in range(len(array)):
        _()
        complited = array[i][9]
        code = array[i][10]
        if complited == None:
            complited = ' '
        if code is None:
            code = ' '
        description = array[i][3]
        address = array[i][4]
        print("{:^3}".format(array[i][0]), "{:^25}".format(array[i][1]), "{:^14}".format(array[i][2]),
          "{:^30}".format(description[:28]), "{:^30}".format(address[:28]), "{:^25}".format(array[i][5]),
          "{:^25}".format(array[i][6]), "{:^8}".format(array[i][7]),
          "{:^10}".format(array[i][8]), "{:^10}".format(complited), "{:^5}".format(code), sep='|')
    print()
def printtable_clients(table):
    print()
    print("{:^3}".format('id'), "{:^25}".format('name'), "{:^14}".format('contact_number'),
          "{:^30}".format('email'), "{:^10}".format('face'), "{:^40}".format('company'), sep='|')
    def _():
        for i in range(194):
            print('-', end='')
        print()

    array = []
    for i in table:
        array.append(i)

    for i in range(len(array)):
        _()
        if array[i][5] == None:
            company = ' '
        else:
            company = array[i][5]
            company = company[:35]
        print("{:^3}".format(array[i][0]), "{:^25}".format(array[i][1]), "{:^14}".format(array[i][2]),
                "{:^30}".format(array[i][3]), "{:^10}".format(array[i][4]), "{:^40}".format(company), sep='|')
    print()
def printtable_products(table):
    print()
    print("{:^3}".format('id'), "{:^25}".format('name'), "{:^5}".format('code'), sep='|')
    def _():
        for i in range(38):
            print('-', end='')
        print()

    array = []
    for i in table:
        array.append(i)

    for i in range(len(array)):
        _()
        print("{:^3}".format(array[i][0]), "{:^25}".format(array[i][1]),
              "{:^5}".format(array[i][2]), sep='|')
    print()
def printtable_reviews(table):
    print()
    print("{:^3}".format('id'), "{:^25}".format('name'), "{:^50}".format('text'),
          "{:^10}".format('date'), "{:^14}".format('contact_number'), sep='|')

    def _():
        for i in range(102):
            print('-', end='')
        print()

    array = []
    for i in table:
        array.append(i)

    for i in range(len(array)):
        _()
        date = str(array[i][3])
        text = array[i][2]
        print("{:^3}".format(array[i][0]), "{:^25}".format(array[i][1]),
              "{:^50}".format(text[:45]), "{:^10}".format(date),
              "{:^14}".format(array[i][4]), sep='|')
    print()
def taskcreator(user):
    try:
        _user = user
        client_name = input('Имя клиента: ')
        contact_number = input('+7')
        while contact_number.isalpha():
            print('Try again')
            contact_number = input('+7')
        cursor.execute('select * from crm.schema_crm.\"ClientsDATATable\" where contact_number =  %(contact_number)s',
                       {'contact_number': int(contact_number)})
        if cursor.fetchall() == []:
            print('Этого контакта не существует')
            taskcreator(user)
        cursor.execute('select * from crm.schema_crm.\"ClientsDATATable\" where contact_number =  %(contact_number)s and name = %(client_name)s',
                       {'contact_number': int(contact_number), 'client_name': client_name})
        if cursor.fetchall() == []:
            print('Контакт не соответствует имени')
            taskcreator(user)
        contact_number = int(contact_number)
        description = input('Описание: ')
        address = input('Адресс: ')
        if user != 'admin':
            cursor.execute('select id from crm.schema_crm.\"EmployeesDATAccounts\" where login = %(user)s', {'user': user})
            id = int(cursor.fetchall()[0][0])
            cursor.execute('select name from crm.schema_crm.\"EmployeesDATATable\" where id = %s', (id,))
            author_name = cursor.fetchall()[0][0]
        else:
            author_name = input('Имя автора: ')
        cursor.execute('select * from crm.schema_crm.\"EmployeesDATATable\" where name = %s', (author_name,))
        executor_name = input('Имя исполнителя: ')
        cursor.execute('select * from crm.schema_crm.\"EmployeesDATATable\" where name = %s', (executor_name,))
        if cursor.fetchall() == []:
            print('Такого работника нет')
            taskcreator(user)
        in_work = 'True'
        today = datetime.now()
        created = str(today.strftime("%d/%m/%y"))
        code_of_product = input('Код продукта: ')
        if code_of_product != '':
            if code_of_product.isdigit():
                code_of_product = int(code_of_product)
            else:
                print('Не удалось добавить код продукта')
                code_of_product = None
        else:
            code_of_product = None
        cursor.execute(
            'insert into crm.schema_crm.\"TasksTable\" (client_name, contact_number, description, address, author_name, executor_name, in_work, created, code_of_product)'
            ' values (%(client_name)s, %(contact_number)s, %(description)s, %(address)s, %(author_name)s, %(executor_name)s, %(in_work)s, %(created)s, %(code_of_product)s)',
            {'client_name': client_name, 'contact_number': contact_number, 'description': description, 'address': address,
             'author_name': author_name, 'executor_name': executor_name, 'in_work': in_work,
             'created': created, 'code_of_product': code_of_product})
        conn.commit()
        main(user)
    except(KeyboardInterrupt, EOFError):
        print()
        exit()
def taskupdate(user):
    id = int(input('ID таска: '))

    cursor.execute('select id from crm.schema_crm.\"EmployeesDATAccounts\" where login = %(user)s',
                   {'user': user})
    _id = int(cursor.fetchall()[0][0])
    cursor.execute('select role from crm.schema_crm.\"EmployeesDATATable\" where id = %s', (_id,))
    role = cursor.fetchall()[0][0]
    if role == 'manager':
        __column = input('Выберите поле для редактирования\n'
                       '1)client_name \n2)contact_number \n3)description \n4)address \n'
                       '5)executor_name \n6)in_work \n7)created \n8)completed \n9)code_of_product \n')
        _column = {1 : 'client_name', 2: 'contact_number', 3 : 'description', 4:'address',5:'executor_name',
                   6:'in_work',7:'created',8:'completed',9:'code_of_product'}

        if __column.isalpha():
            print('Неверный формат ввода\n')
            taskupdate(user)
        __column = int(__column)
        if __column == 8:
            print('Формат ввода: dd/mm/yy\n')
        column = _column.get(__column)
        value = str(input('Введите значение '))
    if role == 'employee':
        column = 'completed'
        today = datetime.now()
        value = str(today.strftime("%d/%m/%y"))
        cursor.execute('update crm.schema_crm.\"TasksTable\" set in_work = \'False\' where id = %s' , (id,))
        conn.commit()
    cursor.execute('update crm.schema_crm.\"TasksTable\" set ' + column + ' = %(value)s where  id = %(id)s',
                   {'id': id, 'value': str(value)})
    cursor.execute('select * from crm.schema_crm.\"TasksTable\" where id = %(id)s', {'id': id})
    printtable(cursor)
    conn.commit()
    main(user)
def taskdelete(user):
    id = int(input('ID таска: '))
    cursor.execute('select * from crm.schema_crm.\"TasksTable\" where id = %(id)s', {'id': id})
    printtable(cursor)
    if int(input('Вы уверены? 1)да 2)нет \n')) == 1:
        cursor.execute('delete from crm.schema_crm.\"TasksTable\" where id = %(id)s', {'id': id})
        conn.commit()
    else:
        main(user)
def taskview(user):
    _user = user
    id = input('ID таска \nдля отображения всего списка нажмите Enter \n')
    if id == '' and user != 'admin':
        while True:
            try:
                cursor.execute('select id from crm.schema_crm.\"EmployeesDATAccounts\" where login = %(user)s',
                               {'user': user})
                id = int(cursor.fetchall()[0][0])
                cursor.execute('select name from crm.schema_crm.\"EmployeesDATATable\" where id = %s', (id,))
                author_name = cursor.fetchall()[0][0]
                cursor.execute('select * from crm.schema_crm.\"TasksTable\" where author_name = %(user)s or executor_name = %(user)s', {'user': author_name} )
                break
            except(psycopg2.errors.UndefinedColumn):
                print('Нет прав доступа\n')
                taskview(user)
        printtable(cursor)
        main(user)
    elif id.isdigit() and user != 'admin':
        id = int(id)
        while True:
            try:
                cursor.execute('select id from crm.schema_crm.\"EmployeesDATAccounts\" where login = %(user)s',
                               {'user': user})
                _id = int(cursor.fetchall()[0][0])
                cursor.execute('select name from crm.schema_crm.\"EmployeesDATATable\" where id = %s', (_id,))
                author_name = cursor.fetchall()[0][0]
                cursor.execute('select * from crm.schema_crm.\"TasksTable\" where id = %(id)s and author_name = %(user)s or id = %(id)s and executor_name = %(user)s' , {'id': id, 'user': author_name})
                break
            except(psycopg2.errors.UndefinedColumn):
                print('нет прав доступа\n')
                taskview(user)
        printtable(cursor)
        main(user)
    elif user == 'admin' and id.isdigit():
        cursor.execute('select * from crm.schema_crm.\"TasksTable\" where id = %(id)s' , {'id': id})
        printtable(cursor)
        main(user)
    elif user == 'admin':
        cursor.execute('select * from crm.schema_crm.\"TasksTable\"')
        printtable(cursor)
        main(user)
    else:
        print('Неверный формат ввода\n')
        main(user)
def clientcreate(user):
    name = input('Имя и фамилия: \n')
    contact_number = input('Номер телефона +7')
    while contact_number.isalpha():
        print('Попробуйте снова\n')
        contact_number = input('Номер телефона +7')
    contact_number = int(contact_number)
    email = input('Email: ')
    face = int(input('1)физ.лицо '
                     '2)юр.лицо \n'))
    while face != 1 and face != 2:
        face = int(input('Попробуйте еще раз \n'
                     '1)физ.лицо '
                     '2)юр.лицо \n'))
    if face == 1:
        face = 'физ.лицо'
    else:
        face = 'юр.лицо'
    company = ''
    if face == 'юр.лицо':
        company = input('Компания \n')
    cursor.execute('insert into crm.schema_crm.\"ClientsDATATable\" (name, contact_number, email, face, company)'
                       ' values (%(name)s, %(contact_number)s, %(email)s, %(face)s, %(company)s)',
                       {'name': name, 'contact_number': contact_number, 'email': email, 'face': face,
                        'company': company})
    conn.commit()
    main(user)
def clientupdate(user):
    search = input('Введите Имя или номер телефона \n')
    # Поиск по имени
    if search.isalpha():
        cursor.execute('select * from crm.schema_crm.\"ClientsDATATable\" where name = %(search)s', {'search': search})
        for i in cursor:
            print(i)
        id = input('ID Клиента \n')
        incefc = int(input('Что необходимо изменить: 1)name,\n 2)contact_number,\n 3)email,\n 4)face,\n 5)company \n'))
        if incefc == 1:
            new_name = input('Новое имя: \n')
            cursor.execute('update crm.schema_crm.\"ClientsDATATable\" set name = %(new_name)s where id = %(id)s',
                           {'new_name': new_name, 'id': id})
            conn.commit()
            main(user)
        elif incefc == 2:
            new_number = input('Номер телефона +7')
            while new_number.isalpha():
                print('Попробуйте снова\n')
                new_number = input('Номер телефона +7')
            new_number = int(new_number)
            cursor.execute(
                'update crm.schema_crm.\"ClientsDATATable\" set contact_number = %(new_number)s where id = %(id)s',
                {'new_number': new_number, 'id': id})
            conn.commit()
            main(user)
        elif incefc == 3:
            new_email = input('Email: ')
            cursor.execute('update crm.schema_crm.\"ClientsDATATable\" set email = %(new_email)s where id = %(id)s',
                           {'new_email': new_email, 'id': id})
            conn.commit()
            main(user)
        elif incefc == 4:
            new_face = input()
            cursor.execute('update crm.schema_crm.\"ClientsDATATable\" set face = %(new_face)s where id = %(id)s',
                           {'new_face': new_face, 'id': id})
            conn.commit()
            main(user)
        elif incefc == 5:
            new_comp = input()
            cursor.execute('update crm.schema_crm.\"ClientsDATATable\" set company = %(new_comp)s where id = %(id)s',
                           {'new_comp': new_comp, 'id': id})
            conn.commit()
            main(user)
        else:
            print('Something went wrong\n')
            main(user)
    elif search.isdigit():
        search = int(search)
        cursor.execute('select * from crm.schema_crm.\"ClientsDATATable\" where contact_number = %(search)s',
                       {'search': search})
        for i in cursor:
            print(i)
        incefc = int(input('Что необходимо изменить: 1)name, 2)contact_number, 3)email, 4)face, 5)company'))
        if incefc == 1:
            new_name = input('Новое имя: \n')
            cursor.execute(
                'update crm.schema_crm.\"ClientsDATATable\" set name = %(new_name)s where contact_number = %(search)s',
                {'new_name': new_name, 'search': search})
            conn.commit()
            main(user)
        elif incefc == 2:
            new_number = input('Номер телефона +7')
            while new_number.isalpha():
                print('Попробуйте снова\n')
                new_number = input('Номер телефона +7')
            cursor.execute(
                'update crm.schema_crm.\"ClientsDATATable\" set contact_number = %(new_number)s where contact_number = %(search)s',
                {'new_number': new_number, 'search': search})
            conn.commit()
            main(user)
        elif incefc == 3:
            new_email = input('Email: ')
            cursor.execute(
                'update crm.schema_crm.\"ClientsDATATable\" set email = %(new_email)s where contact_number = %(search)s',
                {'new_email': new_email, 'search': search})
            conn.commit()
            main(user)
        elif incefc == 4:
            new_face = input()
            cursor.execute(
                'update crm.schema_crm.\"ClientsDATATable\" set face = %(new_face)s where contact_number = %(search)s',
                {'new_face': new_face, 'search': search})
            conn.commit()
            main(user)
        elif incefc == 5:
            new_comp = input()
            cursor.execute(
                'update crm.schema_crm.\"ClientsDATATable\" set company = %(new_comp)s where contact_number = %(search)s',
                {'new_comp': new_comp, 'search': search})
            conn.commit()
            main(user)
        else:
            print('Something went wrong\n')
            main(user)
    else:
        print('Something went wrong \n')
        main(user)
def clientdelete(user):
    search = input('Введите Имя или номер телефона\n')
    if search.isalpha():
        lastname = input('Введите фамилию\n')
        search += ' ' + lastname
        cursor.execute('select * from crm.schema_crm.\"ClientsDATATable\" where name = %(search)s',
                       {'search': search})
        printtable_clients(cursor)
        id = input('ID Клиента ')
        delete = int(input('Удалить запись? 1)да 2)нет '))
        if delete == 1:
            cursor.execute('delete from crm.schema_crm.\"ClientsDATATable\" * where id = %(search)s',
                       {'search': id})
            conn.commit()
    elif search.isdigit():
        cursor.execute('select * from crm.schema_crm.\"ClientsDATATable\" where contact_number = %(search)s',
                       {'search': search})
        printtable_clients(cursor)
        delete = int(input('Удалить запись? 1)да 2)нет '))
        if delete == 1:
            cursor.execute('delete from crm.schema_crm.\"ClientsDATATable\" * where contact_number = %(search)s',
                       {'search': search})
            conn.commit()
        elif delete == 2:
            main(user)
    else:
        print('Неверный формат ввода')
        main(user)
def clientsearch(user):
    search = input('Введите Имя или номер телефона.\nДля отображения всех записей нажмите Enter.\n')
    # Поиск по имени
    if search.isalpha():
        lastname = input('Введите фамилию \n')
        search += ' ' + lastname
        cursor.execute('select * from crm.schema_crm.\"ClientsDATATable\" where name = %(search)s',
                       {'search': search})
        printtable_clients(cursor)
        main(user)
    # Поиск по номеру
    elif search.isdigit():
        search = int(search)
        cursor.execute('select * from crm.schema_crm.\"ClientsDATATable\" where contact_number = %(search)s',
                       {'search': search})
        printtable_clients(cursor)
        main(user)
    elif search == '':
        cursor.execute('select * from crm.schema_crm.\"ClientsDATATable\"')
        printtable_clients(cursor)
        main(user)
    else:
        print('Неверный формат ввода')
        main(user)
def productsearch(user):
    search = input('Имя или код продукта\nДля отображения всего списка нажмите Enter:')
    if search.isalpha():
        cursor.execute('select * from crm.schema_crm.products where name = %s', (search,))
        printtable_products()
        main(user)
    elif search.isdigit():
        cursor.execute('select * from crm.schema_crm.products where code = %s', (search,))
        printtable_products(cursor)
        main(user)
    elif search == '':
        cursor.execute('select * from crm.schema_crm.products')
        printtable_products(cursor)
        main(user)
    else:
        print('Не найдено')
        main(user)
def reviewsearch(user):
    search = input('Имя или номер телефона\n '
                   'Если хотите посмотреть все записи нажмите Enter: ')
    if search == '':
        cursor.execute('select * from crm.schema_crm.\"Reviews\" ')
        printtable_reviews(cursor)
        main(user)
    if search.isalpha():
        cursor.execute('select * from crm.schema_crm.\"Reviews\" where name = %s', (search,))
        printtable_reviews(cursor)
        main(user)
    elif search.isdigit():
        cursor.execute('select * from crm.schema_crm.\"Reviews\" where code = %s', (search,))
        printtable_reviews(cursor)
        main(user)
    else:
        print('Неверный формат ввода')
        main(user)
while True:
    try:
        user = input('login ')
        password = getpass.getpass('password ')
        conn = psycopg2.connect(dbname='crm', user=user, password=password, host='localhost')
        cursor = conn.cursor()
        break
    except(psycopg2.OperationalError):
        print('Упс. Попробуйте еще раз.\n')
    except(KeyboardInterrupt, EOFError):
        exit()

def main(user):
    try:
        choise = int(input('1)управление тасками \n'
                           '2)управление клиентами \n'
                           '3)просмотр продуктов \n'
                           '4)просмотр отзывов \n'))
        if choise == 1:
            query = int(input('1)добавление тасков \n2)редактирование тасков \n3)удаление тасков \n4)просмотр тасков \n'))
            if query == 1:
                taskcreator(user)
            elif query == 2:
                taskupdate(user)
            elif query == 3:
                taskdelete(user)
            elif query == 4:
                taskview(user)
            else:
                print('Неверный формат ввода\n')
                main(user)
        #управление клиентами
        elif choise == 2:
            query = int(input('1)добавление новой записи \n'
                              '2)редактирование записи \n'
                              '3)удаление записи \n'
                              '4)поиск записи \n'))
            if query == 1:
                clientcreate(user)
            elif query == 2:
                clientupdate(user)
            elif query == 3:
                clientdelete(user)
            elif query == 4:
                clientsearch(user)
            else:
                print('Неверный формат ввода\n')
                main(user)
        #просмотр продуктов
        elif choise == 3:
            productsearch(user)
        #просмотр отзывов
        elif choise == 4:
            reviewsearch(user)
        else:
            print('Неверный формат ввода\n')
            main(user)
    except(KeyboardInterrupt, EOFError):
        cursor.close()
        conn.close()
        print()
        exit()
while True:
    try:
        main(user)
    except(ValueError):
        print('Некоректный ввод данных\n')
