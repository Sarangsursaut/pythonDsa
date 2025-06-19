# Ask user for number to the users
n = int(input("Enter how many terms you want in Fibonacci series: "))
# First two numbers are
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
  print(a, end=" ")
  c = a + b
  a = b
  b = c
