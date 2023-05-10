def is_between(n):
    if -2**31 <= n <= 2**31-1:
        return True
    else:
        return False
n = int(input())
