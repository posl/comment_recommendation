def is_greater_than(n):
    if n == 1:
        return True
    else:
        return 2*is_greater_than(n-1) > n*n
n=int(input())
