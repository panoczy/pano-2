#!/usr/bin/env python3

import sys
try:
    a = int(sys.argv[1]) - int(3500)
except(ValueError,IndexError):
    print("Parameter Error")
else:
    if a <= 0:
        b = 0
    elif a <= 1500 and a > 0:
        b = a * 0.03 - 0
    elif a > 1500 and a <= 4500:
        b = a * 0.1 - 105
    elif a > 4500 and a <= 9000:
        b = a * 0.2 - 555
    elif a > 9000 and a <= 35000:
        b = a * 0.25 - 1005
    elif a > 35000 and a <= 55000:
        b = a * 0.3 - 2755
    elif a > 55000 and a <= 80000:
        b = a * 0.35 - 5505
    else:
        b = a * 0.45 - 13505
    print(format(b,".2f"))
