name = "Erin Sophia V. Estrella"
Act = "Exercise 2 - multiply two numbers from user input"
Sec = "BSIS 3A-G2"

print(name)
print(Sec)
print(Act)

def multiply():
    print("**Multiplication**")

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    num1 = float(num1)
    num2 = float(num2)

    answer = num1 * num2

    print(num1, "x", num2, "=", answer)

repeat = "yes"

while repeat == "yes":
    multiply()
    repeat = input("Do you want to multiply again? ")

print("Program ended")