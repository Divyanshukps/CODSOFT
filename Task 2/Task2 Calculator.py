def calculator():
    print("\nSimple Calculator")
    print("------------------")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
            op = input("Choose operation (+, -, *, /): ").strip()
            
            if op == '+':
                result = num1 + num2
                print(f"\nResult: {num1} + {num2} = {result}")
            elif op == '-':
                result = num1 - num2
                print(f"\nResult: {num1} - {num2} = {result}")
            elif op == '*':
                result = num1 * num2
                print(f"\nResult: {num1} * {num2} = {result}")
            elif op == '/':
                if num2 == 0:
                    print("Error: Division by zero!")
                else:
                    result = num1 / num2
                    print(f"\nResult: {num1} / {num2} = {result}")
            else:
                print("Invalid operation! Please choose +, -, *, or /.")
            
            # Ask if user wants another calculation
            another = input("\nPerform another calculation? (y/n): ").lower()
            if another != 'y':
                print("\nCalculator closed.")
                break
        
        except ValueError:
            print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    calculator()
