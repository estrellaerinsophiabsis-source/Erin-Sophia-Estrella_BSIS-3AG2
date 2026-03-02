import math

number = "Exercise 1 - Area of the circle"
name = "Erin Sophia V.Estrella"
section = "BSIS 3AG2"

print(number)
print(name)
print(section)

while True:
    radius = float(input("Enter the radius of the circle: "))

    area = math.pi * radius ** 2
    print(f"The area of the circle is: {area:.2f}")

    again = input("Do you want to calculate again? (Yes/No): ").lower()
    if again != "yes":
        print("Program ended.")
        break