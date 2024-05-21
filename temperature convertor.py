def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

if __name__ == "__main__":
    while True:
        print("\n1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius")
        elif choice == "2":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
