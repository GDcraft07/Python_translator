class CheckPassword:
    def __init__(self, password):
        self.password = password
        self.flags = True
        self.flag_of_alf = False
        self.lists = []
        self.alfavit_rus_and_eng = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm',
                                    'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю', '1234567890']

    def checking_password(self):
        for i in list(self.password):
            try:
                int(i)
                self.lists.append(True)
            except ValueError:
                self.lists.append(False)

        if True in self.lists:
            self.flags = False

        len_flag = len(self.password) > 8

        if self.password.isupper() or self.password.islower():
            flag_upper_or_lower_password = True
        else:
            flag_upper_or_lower_password = False

        password_lower = self.password.lower()

        for i in self.alfavit_rus_and_eng:
            for j in range(len(i) - 2):
                if i[j: j + 3] in password_lower:
                    self.flag_of_alf = True

        if not len_flag or self.flags or flag_upper_or_lower_password or self.flag_of_alf\
                or self.password.isdigit():
            return False
        else:
            return True
