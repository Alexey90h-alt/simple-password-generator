import random
import string

# Приветствие
print("--- Простой генератор паролей ---")

# Спрашиваем у пользователя длину пароля 
password_length = int(input("Введите нужную длину пароля: "))

# Собираем набор символов: буквы, цифры и знаки пунктуации
all_characters = string.ascii_letters + string.digits + string.punctuation

# Генерируем пароль: выбираем случайные символы из набора
# password — это результат, который мы выведем в конце
password = "".join(random.choice(all_characters) for i in range(password_length))

# Вывод результата
print("Ваш готовый пароль:")
print(password)
print("---------------------------------")