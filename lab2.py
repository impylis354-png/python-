import math


def get_input_data():
    """Ввод данных пользователем"""
    d1 = float(input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) => "))
    d2 = float(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы) => "))
    h = float(input("Введите боковое смещение между спасателем и утопающим, h (ярды) => "))
    v_sand = float(input("Введите скорость движения спасателя по песку, v_sand (мили в час) => "))
    n = float(input("Введите коэффициент замедления спасателя при движении в воде, n => "))
    theta1_deg = float(input("Введите направление движения спасателя по песку, theta1 (градусы) => "))

    return d1, d2, h, v_sand, n, theta1_deg


def calculate_time(d1, d2, h, v_sand, n, theta1_deg):
    """Вычисление времени достижения утопающего"""

    theta1 = math.radians(theta1_deg)

    d1_ft = d1 * 3
    h_ft = h * 3

    x = d1_ft * math.tan(theta1)
    s1 = math.sqrt(d1_ft ** 2 + x ** 2)

    s2 = math.sqrt((h_ft - x) ** 2 + d2 ** 2)

    v_sand_fts = v_sand * 5280 / 3600
    v_water_fts = v_sand_fts / n

    time = s1 / v_sand_fts + s2 / v_water_fts

    return time


def print_result(theta1_deg, time):
    """Вывод результата"""
    print(
        f"\nЕсли спасатель начнёт движение под углом theta1, "
        f"равным {theta1_deg:.0f} градусов, "
        f"он достигнет утопающего через {time:.1f} секунды."
    )


# -------------------
# МОДУЛЬНЫЕ ТЕСТЫ
# -------------------

assert round(calculate_time(8, 10, 50, 5, 2, 39.413), 1) == 39.9
assert calculate_time(8, 10, 50, 5, 2, 39.413) > 0

t1 = calculate_time(8, 10, 50, 5, 2, 39.413)
t2 = calculate_time(8, 10, 50, 5, 4, 39.413)

assert t2 > t1

print("Все тесты пройдены успешно!")

# -------------------
# ОСНОВНАЯ ПРОГРАММА
# -------------------

d1, d2, h, v_sand, n, theta1_deg = get_input_data()

time = calculate_time(d1, d2, h, v_sand, n, theta1_deg)

print_result(theta1_deg, time)