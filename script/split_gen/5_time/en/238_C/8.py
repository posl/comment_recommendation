def solve(n):
    if n < 10:
        return n
    else:
        return 9 + (n-10)//10
