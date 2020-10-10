n1 = int(input("First number: ")) 
n2  = int(input("Second number: ")) 
print("The sum of {0} and {1} is {2}" .format(n1, n2, (lambda a, b : a + b)(n1,n2) ))