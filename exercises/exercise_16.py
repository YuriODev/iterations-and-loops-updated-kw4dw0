# Your solution to Exercise 16
num = int(input("Enter a number: "))

for i in range(1, num + 1):
  print(" "*(num - i)+"#"*i)
