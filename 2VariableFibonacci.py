'''
Demonstration of a version of the Fibonacci
algorithm that I came up with
that uses only two variables
excluding the input variable
'''
n1 = 0
n2 = 1

## Note: this does not display the initial
## 0 and 1 in the sequence but can be
## easily adjusted if needed
termNumber = int(input("Please enter the number of terms you would like to print in the Fibonacci sequence."))
for i in range(0,termNumber):
	print(n1+n2)
	n2 = n1+n2
	n1 = n2-n1
