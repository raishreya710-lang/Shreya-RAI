# ==========================================
# Python Programming Internship - Task 1
# Core Python Challenges
# ==========================================


# 1. Sum of Two Numbers
print("\n--- 1. Sum of Two Numbers ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = num1 + num2

print("Sum =", sum_result)


# ==========================================


# 2. Odd or Even Checker
print("\n--- 2. Odd or Even Checker ---")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")


# ==========================================


# 3. Factorial Calculation
print("\n--- 3. Factorial Calculation ---")

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, num + 1):
        factorial = factorial * i

    print("Factorial of", num, "=", factorial)


# ==========================================


# 4. Fibonacci Sequence
print("\n--- 4. Fibonacci Sequence ---")

n = int(input("Enter the number of Fibonacci terms: "))

a = 0
b = 1

if n <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci Sequence:")

    for i in range(n):
        print(a, end=" ")

        a, b = b, a + b

    print()


# ==========================================


# 5. String Reverse
print("\n--- 5. String Reverse ---")

text = input("Enter a string: ")

reversed_text = text[::-1]

print("Reversed string:", reversed_text)


# ==========================================


# 6. Palindrome Check
print("\n--- 6. Palindrome Check ---")

text = input("Enter a word or string: ")

# Convert to lowercase
text = text.lower()

if text == text[::-1]:
    print("It is a Palindrome.")
else:
    print("It is NOT a Palindrome.")


# ==========================================


# 7. Leap Year Check
print("\n--- 7. Leap Year Check ---")

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year.")
else:
    print(year, "is NOT a Leap Year.")


# ==========================================


# 8. Armstrong Number
print("\n--- 8. Armstrong Number ---")

num = int(input("Enter a number: "))

# Number of digits
order = len(str(num))

# Calculate sum of digits raised to the power of order
sum_val = sum(int(digit) ** order for digit in str(num))

if num == sum_val:
    print(num, "is an Armstrong number.")
else:
    print(num, "is NOT an Armstrong number.")


# ==========================================
# End of Task 1
# ==========================================-