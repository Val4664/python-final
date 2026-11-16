"""
    main.py
    Вариант 10. Расход воды в квартире
    Автор: Колпаков Владислав
    Назначение: Программа для расчета расхода воды в квартире.
"""

def get_resident_count():
    """Запрашивает количество жильцов и проверяет его допустимый диапазон."""
    resident_count = None

    while resident_count is None or not (0 < resident_count <= 10):
        resident_count = int(input("Введите количество жильцов (от 1 до 10): "))

    return resident_count

def get_daily_consumption():
    """Запрашивает суточный расход воды и проверяет его неотрицательность."""
    daily_water_consumption = None

    while daily_water_consumption is None or daily_water_consumption < 0:
        daily_water_consumption = float(input("Введите суточный расход воды (в литрах): "))

    return daily_water_consumption

def get_apartment_type(consumption):
    """
    Определяет категорию расхода воды на одного человека.

    Параметр:
        consumption — суточный расход воды на одного жильца.
    """
    match consumption:
        case value if value <= 100:
            return "Экономный"
        case value if value <= 150:
            return "В пределах нормы"
        case _:
            return "Превышение"

def print_report(resident_count, daily_water_consumption, apartment_type):
    """
    Рассчитывает показатели квартиры и выводит отчет.

    Параметры:
        resident_count — количество жильцов.
        daily_water_consumption — общий суточный расход воды.
        apartment_type — категория расхода воды.
    """
    water_consumption_per_resident = daily_water_consumption / resident_count
    normative_consumption = NORM * resident_count
    percentage_of_norm = daily_water_consumption / normative_consumption * 100

    print(f"\n{'ОТЧЕТ О РАСХОДЕ ВОДЫ':^59}")
    print(f"{'Количество жильцов:':<35}{resident_count:>24}")
    print(f"{'Расход квартиры:':<35}{daily_water_consumption:>22.2f} л")
    print(f"{'Расход на человека:':<35}{water_consumption_per_resident:>22.2f} л")
    print(f"{'Норматив квартиры:':<35}{normative_consumption:>22.2f} л")
    print(f"{'Процент от нормы:':<35}{percentage_of_norm:>23.1f}%")
    print(f"{'Категория:':<35}{apartment_type:>24}")

    print(f"\n{'НАКОПЛЕННЫЙ РАСХОД ЗА ПЕРИОД ОТ 1 ДО 7 ДНЕЙ':^59}")
    print(f"|{'Дни':^10}|{'Фактический расход':^22}|{'Нормативный расход':^23}|")
    print("-" * 59)

    # Выводит накопленный, фактический и нормативный расход за каждый день
    for day in range(1, 8):
        actual_consumption = daily_water_consumption * day
        normative_consumption = NORM * day * resident_count

        print(f"|{day:^10}|{actual_consumption:^22.1f}|{normative_consumption:^23.1f}|")

NORM = 150  # Норматив расхода воды на одного жильца в литрах

def main():
    print("Расход воды в квартире\n")

    # Получение исходных данных с проверкой корректности ввода.
    resident_count = get_resident_count()
    daily_water_consumption = get_daily_consumption()

    # Расчет расхода на одного человека и определение категории.
    water_consumption_per_resident = daily_water_consumption / resident_count
    apartment_type = get_apartment_type(water_consumption_per_resident)

    # Формирование итогового отчета.
    print_report(resident_count, daily_water_consumption, apartment_type)

# Основной цикл повторного выполнения расчетов.
while True:
    main()

    end = input("\nВыполнить новый расчёт? (да/нет): ").strip().lower()

    while end not in ("да", "нет"):
        end = input("Некорректный ввод. Введите 'да' или 'нет': ").strip().lower()

    if end == "нет":
        print("Работа программы завершена.")
        break