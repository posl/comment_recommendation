def max_money(A,B,C):
    max = 0
    if A+B+C > max:
        max = A+B+C
    if A+B*C > max:
        max = A+B*C
    if A*B+C > max:
        max = A*B+C
    if A*B*C > max:
        max = A*B*C
    if (A+B)*C > max:
        max = (A+B)*C
    if A*(B+C) > max:
        max = A*(B+C)
    return max
