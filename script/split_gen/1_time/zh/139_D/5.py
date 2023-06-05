def solve(n):
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    elif n == 3:
        print(2)
    elif n%2 == 0:
        print(n*(n-1)//2)
    else:
        print(n*(n-1)//2 - 1)
