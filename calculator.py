#!/usr/bin/env python3

import sys
def result(argv):
    for s in sys.argv[1:]:
        try :
            number,salary = s.split(':')
            salary = int(salary)
        except(IndexError,ValueError):
            print("Parameter Error")
        else:
            a = salary - 3500 - suf(salary)
            incometax(a)
            print(number+':'+format(salary - incometax(a) - suf(salary),".2f"))
def suf(salary):
    value = salary * 0.165
    return value
def incometax(ratable):
    if ratable <= 0:
        tax = 0
    elif ratable < 1500:
        tax = ratable * 0.03
    elif ratable > 1500 and ratable <= 4500:
        tax = ratable * 0.1 - 105
    elif ratable > 4500 and ratable <= 9000:
        tax = ratable * 0.2 - 555
    elif ratable > 9000 and ratable <= 35000:
        tax = ratable * 0.25 - 1005
    elif ratable > 35000 and ratable <= 55000:
        tax = ratable * 0.3 - 2755
    elif ratable > 55000 and ratable <= 80000:
        tax = ratable * 0.35 - 5505
    else:
        tax = ratable * 0.45 - 13505
    return tax
if __name__ == '__main__':
    result(sys.argv[1:])
