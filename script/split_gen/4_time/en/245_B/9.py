def check(a, b):
    if (a >= 0 and b >= 0):
        return True
    else:
        return False
N = int(input())
A = list(map(int, input().split()))
A.sort()
