print("Welcome to dectobin")

while True:
    decimal = input("Enter a decimal integer: ")
    try:
        decimal = int(decimal)
        break
    except:
        print("\nPlease enter a valid decimal integer")

print("\n{} in binary is {}".format(decimal, bin(decimal)[2:]))
