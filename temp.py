import sys

sys.setrecursionlimit(2000)
from math import comb
from decimal import Decimal


def repeatedly_divide(ch, m, i):
    for j in range(i):
        ch = Decimal(ch / m)
    return ch

def overflow_prop(n, k, m):
    sum = 0

    nk = n * k

    for i in range(17, nk + 1):
        if i == 162:
            asd = 234
        ch = comb(nk, i)
        ch = repeatedly_divide(ch, m, i)
        # x = (1 / m) ** i
        y = Decimal((1 - 1 / m) ** (nk - i))
        prod = ch * y
        sum += prod

    return sum

def overflow_prop2(n, k, m, count):
    sum = Decimal(0)

    nk = n * k

    # From 0 to count
    for i in range(count + 1):
        ch = comb(nk, i)
        # ch = repeatedly_divide(ch, m, i)
        x = (Decimal(1 / m)) ** i
        y = (Decimal(1 - Decimal(1 / m))) ** (nk - i)
        prod = Decimal(ch * x * y)
        print(f'{i} {prod}')
        sum += prod

    return 1 - sum


if __name__ == '__main__':
    n = 100000
    m = 8 * n
    res = overflow_prop2(n, 5, m, 15)
    print(res)
    print(res * m)
