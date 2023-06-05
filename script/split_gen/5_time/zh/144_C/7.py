def solve(n):
    #i*j=n
    #i+j最小
    #i=1~n
    #j=n/i
    #j最小
    import math
    j = math.ceil(math.sqrt(n))
    while j > 0:
        if n % j == 0:
            i = n // j
            return i + j - 2
        j -= 1
