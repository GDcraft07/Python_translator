import sys
from googletrans import Translator
from PyQt5.QtWidgets import QApplication, QMainWindow
from desing import *
from bd_account import *
from PyQt5.QtGui import QPixmap
from bd_history import *

translates_lang = {
    "Английский": ["en", 0],
    "Русский": ["ru", 1],
    "Испанский": ["es", 2],
    "Французский": ["fr", 3],
    "Китайский": ["zh-tw", 4],
    "Немецкий": ["de", 5]
}

translates_lang_1 = {
    "Английский": ["en", 1],
    "Русский": ["ru", 0],
    "Испанский": ["es", 2],
    "Французский": ["fr", 3],
    "Китайский": ["zh-tw", 4],
    "Немецкий": ["de", 5]
}


class Translating:
    def __init__(self, text, src='en', dest='ru'):
        self.text = text
        self.src = src
        self.dest = dest

    def __str__(self):
        try:
            translator = Translator()
            translation = translator.translate(text=self.text, src=self.src, dest=self.dest)
            return translation.text
        except TypeError:
            return self.text


class Account:
    def __init__(self):
        self.reg_name = open('reg_name', 'r', encoding='UTF-8').read()


class History(QMainWindow, HistoryTrans, Account):
    def __init__(self):
        super().__init__()
        self.setupui(self)
        self.initui()

    def initui(self):
        list_history(self.label, self.tableWidget)


class RegWindow(Registrating, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupui(self)
        self.initui()
        self.pixils = None
        self.funk = None

    def initui(self):
        self.setWindowTitle('Войти|Зарегистрироваться')
        self.pixils = QPixmap('logos.png')
        self.logos.setPixmap(self.pixils)
        self.registrates.clicked.connect(self.regs)
        self.sing_in.clicked.connect(self.regs)

    def regs(self):
        if self.sender().text() == 'Зарегистрироваться':
            self.funk = register
        else:
            self.funk = login
        users_login = self.users_login.text()
        users_password = self.users_password.text()

        if self.funk(users_login, users_password, self.error_password):
            self.label_2.setVisible(False)
            self.label_3.setVisible(False)
            self.users_login.setVisible(False)
            self.users_password.setVisible(False)
            self.registrates.setVisible(False)
            self.error_password.setVisible(True)
            self.sing_in.setVisible(False)
            reg_name = open('reg_name', 'w')
            reg_name.write(users_login)
            reg_name.close()
        else:
            self.error_password.setVisible(True)


class Window(MainWindows, QMainWindow, Account):
    def __init__(self):
        super().__init__()
        self.setupui(self)
        self.pushButton.clicked.connect(self.click_translate_button)
        self.pushButton_3.clicked.connect(self.open_history)
        self.pushButton_2.clicked.connect(self.reverse)
        self.pushButton_4.clicked.connect(self.registrate)
        self.setWindowTitle(f'Переводчик ({self.reg_name})')
        self.reg = None
        self.history = None

    def click_translate_button(self):
        text = self.plainTextEdit.toPlainText().split('\n')
        new_text = []
        lang_old_translate = self.comboBox.currentText()
        lang_new_translate = self.comboBox_2.currentText()

        for i in text:
            translate_text = Translating(i, translates_lang[lang_old_translate][0],
                                         translates_lang[lang_new_translate][0])
            new_text.append(str(translate_text))

        new_text = '\n'.join(new_text)
        self.plainTextEdit_2.setPlainText(new_text)
        add_item_table('\n'.join(text), new_text)

    def reverse(self):
        text_combobox = self.comboBox.currentText()
        text_combobox_2 = self.comboBox_2.currentText()
        print(text_combobox, text_combobox_2)
        text_plain_1 = self.plainTextEdit.toPlainText()
        text_plain_2 = self.plainTextEdit_2.toPlainText()
        self.comboBox.setCurrentIndex(translates_lang[text_combobox_2][1])
        self.comboBox_2.setCurrentIndex(translates_lang_1[text_combobox][1])
        self.plainTextEdit.setPlainText(text_plain_2)
        self.plainTextEdit_2.setPlainText(text_plain_1)
        self.click_translate_button()

    def registrate(self):
        self.reg = RegWindow()
        self.reg.show()

    def open_history(self):
        self.history = History()
        self.history.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = Window()
    test.show()
    sys.exit(app.exec())
