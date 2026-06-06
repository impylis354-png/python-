import math


def get_input_data():
    d1 = float(input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) => "))
    d2 = float(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы) => "))
    h = float(input("Введите боковое смещение между спасателем и утопающим, h (ярды) => "))
    v_sand = float(input("Введите скорость движения спасателя по песку, v_sand (мили в час) => "))
    n = float(input("Введите коэффициент замедления спасателя при движении в воде, n => "))

    return d1, d2, h, v_sand, n


def calculate_time(d1, d2, h, v_sand, n, theta1_deg):
    theta1 = math.radians(theta1_deg)

    d1_ft = d1 * 3
    h_ft = h * 3

    x = d1_ft * math.tan(theta1)

    s1 = math.sqrt(d1_ft ** 2 + x ** 2)
    s2 = math.sqrt((h_ft - x) ** 2 + d2 ** 2)

    v_sand_fts = v_sand * 5280 / 3600
    v_water_fts = v_sand_fts / n

    return s1 / v_sand_fts + s2 / v_water_fts


def find_best_angle(d1, d2, h, v_sand, n):
    best_angle = 0
    best_time = float("inf")

    angle = 0

    while angle < 90:
        current_time = calculate_time(
            d1, d2, h, v_sand, n, angle
        )

        if current_time < best_time:
            best_time = current_time
            best_angle = angle

        angle += 0.1

    return best_angle, best_time


# -------------------
# МОДУЛЬНЫЕ ТЕСТЫ
# -------------------

angle, time = find_best_angle(8, 10, 50, 5, 2)

assert 0 <= angle <= 90
assert time > 0

print("Все тесты пройдены успешно!")

# -------------------
# ОСНОВНАЯ ПРОГРАММА
# -------------------

d1, d2, h, v_sand, n = get_input_data()

best_angle, best_time = find_best_angle(
    d1, d2, h, v_sand, n
)

print(f"\nОптимальный угол: {best_angle:.1f} градусов")
print(f"Минимальное время: {best_time:.1f} секунд")

