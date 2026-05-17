# Проект FitLife - MVP версия 1.0
# Импортировал sys так как из-за кодировки тест был с ошибкой
import sys

sys.stdout.reconfigure(encoding='utf-8')

WATER_PER_KG = 30

# Спрашиваем имя пользователя
# При помощи tile переводим первую букву в нижний регистр
user_name = input('Здравствуйте. Как вас зовут: ').title()

# Собираем данные с пользователя, при помощи try except
# Отслеживаем ошибки и если что указываем пользователю на неё
try:
    user_age = int(input('Сколько вам полных лет (пр. 45): '))
except ValueError:
    print("Ошибка: введите целое число (пример: 56)")
    exit()

# Используем replace для замены запятой на точку
try:
    user_weight = float(input('Сколько вы весите в кг (пр. 45.2): ')
                        .replace(',', '.'))
except ValueError:
    print('Ошибка: введите число с точкой (пример: 75.3)')
    exit()

try:
    user_height = float(input('Какой у вас рост в м (пр. 1.55): ')
                        .replace(',', '.'))
except ValueError:
    print('Ошибка: введите число с точкой (пример: 1.65)')
    exit()

# Проводим расчёты
bmi = round(user_weight / (user_height ** 2), 1)
water_ml = user_weight * WATER_PER_KG
water_l = round(water_ml / 1000, 2)

# Выводим результат на экран
print('=' * 30)
print(f'\nОтчет для пользователя: {user_name} ({user_age} лет)')
print(f'Твой индекс массы тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print('\nРасчёт окончен. Не болей и не скучай!)')
