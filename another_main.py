# Variables

# snake_case for python variables
# camelCase for Javascript
# PascalCase for classes of all languages
# kebab-case usually for only file names or html 

num1 = 5
num2 = 7

print(num1 + num2)

num2 = 1

print(num1 + num2) # The program reads top to bottom, so the second printed number will be 6 rather than 12
# Assign the value of num2 to num1
# num1 <- num2
num1 = num2
print(num1 + num2)

num3 = 5

num3 = num3 + 2
print(num3)
total = num1 + num2 + num3
# String interpolation
print("The total  addition is", total)
print(f"The total addition is {total}")