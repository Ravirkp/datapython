try:
    print(10/0)
    name = int(input("Enter the number :"))
    print(name)
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("division by zero")