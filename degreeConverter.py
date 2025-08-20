
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    try:
        a = float(input("Enter the Temperature in Degree Celsius: "))
        fahrenheit = celsius_to_fahrenheit(a)
        print(f"Temperature in Fahrenheit: {fahrenheit}")
    except ValueError:
        print("Please enter a valid number.")
