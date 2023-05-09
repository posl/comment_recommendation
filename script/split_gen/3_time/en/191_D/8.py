def main():
    from sys import stdin
    # from math import ceil
    # from math import floor
    # from decimal import Decimal
    # from decimal import ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_HALF_DOWN
    f_i = stdin
    
    X, Y, R = [float(x) for x in f_i.readline().split()]
    
    # R = Decimal(R)
    # X = Decimal(X)
    # Y = Decimal(Y)
    # R = R.quantize(Decimal('1.0000'), rounding=ROUND_HALF_DOWN)
    # X = X.quantize(Decimal('1.0000'), rounding=ROUND_HALF_DOWN)
    # Y = Y.quantize(Decimal('1.0000'), rounding=ROUND_HALF_DOWN)
    # R = float(R)
    # X = float(X)
    # Y = float(Y)
    R = round(R, 4)
    X = round(X, 4)
    Y = round(Y, 4)
    
    # print(R)
    # print(X)
    # print(Y)
    
    # print(ceil(X+R))
    # print(ceil(Y+R))
    # print(floor(X-R))
    # print(floor(Y-R))
    
    count = 0
    for i in range(int(X-R), int(X+R)+1):
        for j in range(int(Y-R), int(Y+R)+1):
            if (i-X)**2 + (j-Y)**2 <= R**2:
                count += 1
    print(count)
    
    return
