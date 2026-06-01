import math

d1 = float(input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) => "))
d2 = float(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы) => "))
h = float(input("Введите боковое смещение между спасателем и утопающим, h (ярды) => "))
v_sand = float(input("Введите скорость движения спасателя по песку, v_sand (мили в час) => "))
n = float(input("Введите коэффициент замедления спасателя при движении в воде, n => "))
theta1_deg = float(input("Введите направление движения спасателя по песку, theta1 (градусы) => "))

theta1 = math.radians(theta1_deg)

d1_ft = d1 * 3
h_ft = h * 3

x = d1_ft * math.tan(theta1)
s1 = math.sqrt(d1_ft**2 + x**2)

s2 = math.sqrt((h_ft - x)**2 + d2**2)

v_sand_fts = v_sand * 5280 / 3600
v_water_fts = v_sand_fts / n

time = s1 / v_sand_fts + s2 / v_water_fts

print(
    f"\nЕсли спасатель начнёт движение под углом theta1, равным {theta1_deg:.0f} градусов, "
    f"он достигнет утопающего через {time:.1f} секунды."
)