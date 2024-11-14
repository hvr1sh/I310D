def calculate_volume_of_sphere(radius):
    pi = 3.14159265
    volume = (4/3) * radius * radius * radius
    return volume

radius1 = 30
volume1 = calculate_volume_of_sphere(radius1)
print(f"The area of circle with volume {radius1} is: {volume1}")

radius2 = 40
volume2 = calculate_volume_of_sphere(radius2)
print(f"The volume of circle with radius {radius2} is: {volume2}")