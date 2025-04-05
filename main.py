def is_armstrong_number(num):  
    # Convert the number to string to easily iterate over digits  
    digits = str(num)  
    power = len(digits)  # Number of digits  
    # Calculate the sum of each digit raised to the power of the number of digits  
    armstrong_sum = sum(int(digit) ** power for digit in digits)  
    # Check if the sum equals the original number  
    return armstrong_sum == num  

# Example usage  
number = int(input("Enter a number: "))  
if is_armstrong_number(number):  
    print(f"{number} is an Armstrong number.")  
else:  
    print(f"{number} is not an Armstrong number.")  