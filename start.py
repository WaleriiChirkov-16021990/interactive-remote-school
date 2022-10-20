# Данный блок осуществляет авторизацию пользователя в системе \
# и регитсрацию нового.


from registering_a_new_user import registering_a_new_user as r_new
from check_user_input import chek_use_inpt as check


def open_data_user(path):
    list_data = []
    with open(path, 'r', encoding='utf-8') as data:
        line = data.readlines()
        for i in line:
            i.replace(' ', '')
            list_data.append(i.replace('\n', '').split(';'))
    return list_data


def add_record_new_user(base: list, new_user: list, path: str):
    base.append(new_user)
    new_user = ';'.join(new_user)
    with open(path, 'a', encoding='utf-8') as data:
        data.write(f'\n{new_user}')
    return base


def start():
    print('Вас приветствует интерактивный помошник школы!')
    path = 'data_users.txt'
    while True:
        print('Для продолжения выберите действие:\
            \n1.Регистрация\n2.Вход\n3.Завершить работу')
        select_ = None
        user_list = None
        list_data = open_data_user(path)
        select_ = check(1)
        if select_ == '1':
            new_user = r_new()
            if new_user:
                list_data = add_record_new_user(list_data, new_user, path)
            else:
                continue
        elif select_ == '2':
            log_ = check(2, list_data)
            if log_:
                user_list = [i for i in list_data if i[0] == log_]
                user_list = user_list[0]
            else:
                continue
            password = check(3, user_list)
            if password:
                print('')
                # return user_list  эта строка возвращала список авторизованного пользователя
            else:
                continue
        elif select_ == '3':
            return print('Программа завершена')


start()
