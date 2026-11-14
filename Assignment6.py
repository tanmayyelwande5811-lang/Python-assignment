# Tanmay Yelwande
# SY - C 34

# SQUARE OF NUMBERS AND EVEN NUMBERS

# creating a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# lambda function to find square of numbers
square = lambda x: x * x

# using list comprehension with lambda function
squares = [square(x) for x in numbers]

# using list comprehension to find even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

# Displaying the results
print("Original List:", numbers)
print("Squares:", squares)
print("Even Numbers:", even_numbers)


# EMPLOYEE SALARY PROCESSING

# List of employee salaries
salaries = [30000, 45000, 50000, 60000, 70000]

# Lambda function to add 10% bonus
add_bonus = lambda salary: salary + (salary * 10 / 100)

# List comprehension to calculate updated salaries
updated_salaries = [add_bonus(salary) for salary in salaries]

# List comprehension to find salaries greater than 50000
high_salaries = [salary for salary in updated_salaries if salary > 50000]

# Displaying results
print("Original Salaries:", salaries)
print("Salaries After 10% Bonus:", updated_salaries)
print("Salaries Greater than 50000:", high_salaries)