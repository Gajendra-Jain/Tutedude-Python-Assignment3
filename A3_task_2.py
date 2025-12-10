# Math Module Calculator Program
import math

# Get input from user
number = float(input("Enter a number: "))

# Check if the number is valid for all operations
if number <= 0:
    print("Error: Please enter a positive number for logarithm calculation.")
else:
    # Calculate square root
    sqrt_result = math.sqrt(number)
    
    # Calculate natural logarithm (log base e)
    log_result = math.log(number)
    
    # Calculate sine (input is in radians)
    sine_result = math.sin(number)
    
    # Display results
    print(f"Square Root: {sqrt_result}")
    print(f"Logarithm: {log_result}")
    print(f"Sine: {sine_result}")