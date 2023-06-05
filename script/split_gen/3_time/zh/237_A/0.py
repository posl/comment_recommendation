def check(n):
    if n >= -2**31 and n <= 2**31-1:
        return True
    else:
        return False
n = int(input())
