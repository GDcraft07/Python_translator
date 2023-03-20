import sqlite3
from check_password import *


def login(logins, passw, signal):
    con = sqlite3.connect('translate_bd.sqlite')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM account WHERE login="{logins}";')
    value = cur.fetchall()
    if passw == '' or logins == '':
        signal.setText("<html><head/><body><p align=\"center\"><span style=\""
                       " color:#ff0000;\">Проверте ввели ли вы данные!"
                       "</span></p></body></html>")
        flag = False

    elif value != [] and value[0][2] == passw:
        signal.setText('Успешная авторизация!')
        flag = True
    else:
        signal.setText("<html><head/><body><p align=\"center\"><span style=\""
                       " color:#ff0000;\">Проверьте правильность ввода данных!"
                       "</span></p></body></html>")
        flag = False

    cur.close()
    con.close()

    return flag


def register(logins, passw, signal):
    flags = False
    con = sqlite3.connect('translate_bd.sqlite')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM account WHERE login="{logins}";')
    value = cur.fetchall()

    if passw == '' or logins == '':
        signal.setText("<html><head/><body><p align=\"center\"><span style=\""
                       " color:#ff0000;\">Проверте ввели ли вы данные!"
                       "</span></p></body></html>")
        flags = False

    elif not value == []:
        signal.setText("<html><head/><body><p align=\"center\"><span style=\""
                       " color:#ff0000;\">Такой ник уже используется!"
                       "</span></p></body></html>")
        flags = False

    elif not CheckPassword(passw).checking_password():
        signal.setText("<html><head/><body><p align=\"center\"><span style=\""
                       " color:#ff0000;\">Пароль не соответствует стандартам"
                       "</span></p></body></html>")
        flags = False

    elif value == [] and CheckPassword(passw).checking_password():
        cur.execute(f"INSERT INTO account (login, password) VALUES ('{logins}', '{passw}')")
        signal.setText('Вы успешно зарегистрированы!')
        con.commit()
        flags = True

    cur.close()
    con.close()

    return flags
