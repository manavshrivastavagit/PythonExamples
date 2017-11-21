# Fibonacci series:
# the sum of two elements defines the next
limit = int( input('enter the limit : ') )
a, b = 0, 1
while b < limit:
    print ( a )
    a, b = b, a + b