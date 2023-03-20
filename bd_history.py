import sqlite3
import datetime
from PyQt5.QtWidgets import QTableWidgetItem


def add_item_table(first_lang, sec_lang):
    tm = str(datetime.datetime.now())[:16]
    con = sqlite3.connect('translate_bd.sqlite')
    cur = con.cursor()
    account = open('reg_name', encoding='UTF-8').read()

    ids = cur.execute(f"SELECT id FROM account WHERE login = '{account}'").fetchall()[0][0]
    cur.execute(f'''INSERT INTO history (first_lang, sec_lang, acc, date) VALUES ('{first_lang}', '{sec_lang}', 
    '{ids}', '{tm}')''')
    con.commit()

    cur.close()
    con.close()


def list_history(funk, funk_2):
    user = open('reg_name', encoding='UTF-8').read()

    con = sqlite3.connect('translate_bd.sqlite')
    cur = con.cursor()
    funk.setText(f'История аккаунта ({user})')
    cur.execute(f'''SELECT first_lang, sec_lang, date FROM history WHERE 
    acc=(SELECT id FROM account WHERE login = '{user}')''')
    result = cur.fetchall()
    cur.close()
    con.close()
    funk_2.setColumnCount(3)
    funk_2.setRowCount(0)
    funk_2.setHorizontalHeaderLabels(['Первый язык', 'Второй язык', 'Время'])

    for i, row in enumerate(result):
        funk_2.setRowCount(
            funk_2.rowCount() + 1)
        for j, elem in enumerate(row):
            funk_2.setItem(
                i, j, QTableWidgetItem(str(elem)))
