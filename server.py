import hashlib  # библиотека хэширования

razd = '|||'    # разделитель

def update_data():  # обновление data
    f = open('DATA.txt', 'r')   # открытие файла с данными
    data = f.read().split(razd)[:-1]    # создание списка со всеми данными
    f.close()   # закрытие файла
    return data # возврат обновленного списка

def give_salt():    # получение соли
    data = update_data()
    return data[0].encode()

def reg(login, passw, name = ''):  # регистрация пользователя
    data = update_data()
    if login not in data:
        f = open('DATA.txt', 'a')
        f.write(str(login) + razd + str(passw) + razd + str(name) + razd)
        f.close()
        data = update_data()
        return True
    else:
        return False

def check(login, passw):    # проверка введенных данных
    data = update_data()
    client = []
    if login in data:
        if data[data.index(login)+1] == passw:
            client = [data[data.index(login)], data[data.index(login)+2]]
            return client
        else: return client
    else:
        return client
