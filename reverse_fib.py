#!/usr/bin/env python
# usage reverse_fib.py f
# Where f is the fibonacci number to computer the index of.
# No check is made if f is really a fibonacci number.
# f must be > 1
import sys
import math
if len (sys.argv) != 2:
    print 'Usage fib.py f\nWhere f is the fibonacci number.'
    sys.exit(-1)
f = int(sys.argv[1])

golden_ration = golden_ratio = (1 + math.sqrt(5)) / 2

print math.floor(math.log(f * math.sqrt(5) + 0.5, golden_ratio))