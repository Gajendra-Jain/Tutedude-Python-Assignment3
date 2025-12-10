# Factorial Calculator Program

#function to calculate factorial using recursion
def factorial_recursion(n):
    """Calculate factorial using recursion"""
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)


# Main program
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    
    print(f"factorial of {number} is: {factorial_recursion(number)}")