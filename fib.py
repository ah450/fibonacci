#!/usr/bin/env python
# Usage : fib.py n 
# prints the nth fibonacci number
import sys
import math
if len (sys.argv) != 2:
    print 'Usage fib.py n\nWhere n is the index of the fibonacci number.'
    sys.exit(-1)
n = int(sys.argv[1])

golden_ratio = (1 + math.sqrt(5)) / 2
def fib(n):
    return (golden_ratio ** n - (-golden_ratio ** - n ) ) / math.sqrt(5)

if n > 0:
    print math.floor(fib(n))
else:
    print 1