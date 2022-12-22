def fib(n):
  a, b = 0, 1
  for i in range(n):
    print(a)
    a, b = b, a + b


termNumber = int(input("Please enter the number of terms you would like to print in the Fibonacci sequence."))

fib(termNumber)

