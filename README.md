Проект Переводчик.
Основной целью данного проекта было создания собственного переводчика с пользовательским интерфейсом.
Для перевод текста пользователя я использовал библеотеку GoogleTrans.
Для создания пользовательского интерфейса использовалась библеотека PyQt5.
У приложения есть 3 окна:
  1) Основное. На нем пользователь может переводить различные тексты, менять языки и переходить в другие окна.
  2) Окно регестрации. В этом окне пользователь может зарегестрироваться или войти в учетную запись.
  3) Окно с историей. Здесь пользователь может посмотерть свою историю переводов.

Каждое окно взаимодействует с базой данных(для заполнения баз данныж использовал sqlite3)
