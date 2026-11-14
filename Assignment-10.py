# Define a function to divide two numbers
def divide_numbers(num1, num2):
    try:
        # Explicitly check for None if you want a custom ValueError
        if num1 is None or num2 is None:
            raise ValueError("Inputs cannot be None.")
            
        # Attempt to divide the numbers
        result = num1 / num2
        print(f"The result is: {result}")
    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Cannot divide by zero!")
    except TypeError:
        # Handle type mismatch error
        print("Error: Invalid input type. Please enter numbers only.")
    except ValueError as e:
        # Handle value error (e.g., inputs being None or strings)
        print(f"Error: Invalid input value. {e}")
    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")

# Test the function with valid inputs
print("Test 1: Valid inputs")
divide_numbers(10, 2)

# Test the function with division by zero
print("\nTest 2: Division by zero")
divide_numbers(10, 0)

# Test the function with invalid input types
print("\nTest 3: Invalid input types")
divide_numbers("ten", 2)

# Test the function with value error
print("\nTest 4: Value error")
divide_numbers(10, "two")

# Test the function with unexpected exception / None value
print("\nTest 5: Unexpected exception or None input")
divide_numbers(10, None)
