### Подключаем модуль sqlite3
import sqlite3




# Функция создания таблицы

def create_table():
    # Здесь name - название таблицы
    # Создаем запрос на создание таблицы, если таковой еще не существует
    que_create = '''
        CREATE TABLE IF NOT EXISTS SCHOT(
            id INTEGER PRIMARY KEY,
            You INTEGER,
            Vrag INTEGER
        )
    '''

    # С помощью курсора выполняем запрос
    cur.execute(que_create)
    # Сохраняем изменения в базе данных
    database.commit()

# Функция получения данных
def get_data():
    # Здесь column - поля таблицы, которые хотим получить(столбцы)
    # table_name - имя таблицы, из которой хотим получить данные
    # Создаем запрос на получение данных
    que_select = '''
        SELECT You FROM SCHOT'
    '''

    # Получаем результат
    result = cur.execute(que_select)
    # Получаем все строки из результата
    data = result.fetchall()
    # Возвращаем полученные строки
    return data

# Функция занесения данных в таблицу
def insert_data(SCHOT, You, Vrag, a, b):
    # Здесь table_name - название таблицы, в которую хотите занести данные
    # column - поля(столбцы) в которые хотите занести данные
    # value - сами данные
    # Создаем запрос на внесение данных в таблицу
    que_insert = '''
            INSERT INTO SCHOT (You) VALUES (a) 
        '''
    a = 1
    b = 2
    # С помощью курсора выполняем запрос
    cur.execute(que_insert)
    # Сохраняем изменения в базе данных
    database.commit()


# Создаем подключение в базе данных
database = sqlite3.connect('game.sqlite')

# Создаем курсор, который дальше будет общаться с базой
cur = database.cursor()

# Вызываем функцию создания таблицы с названием 'scores'
create_table()
# Вносим в таблицу с названием 'scores' данные
# Обратите внимание, что вторым аргументом вводятся поля(колонки/столбцы), в которые вы хотите внести данные. Вводятся они через запятую и через пробел
# Третьим аргументом идут сами данные. Обратите внимание, что здесь стоят двойные кавычки("")
# Чтобы ввести текстовые данные, необходимо поставить еще и одинарные кавычкы, иначе работать НЕ БУДЕТ
a = 1
b = 2
insert_data('SCHOT', 'You, Vrag', 'a, b')
insert_data('scores', 'name, score', "'Иван', 10")
# Выводим данные. Обратите внимание, что поля, которые вы хотите вывести, необходимо писать через запятую и пробел
# Сначала пишется название таблицы, из которой хотите получить данные, после этого пишутся поля
a = get_data('scores', 'name, score')
b = get_data('scores', 'name, score')

# Закрываем соединение с базой данных
database.close()
###