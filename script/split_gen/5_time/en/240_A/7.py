def check(a,b):
    if (a < b) and (1 <= a) and (b <= 10):
        return True
    else:
        return False
a,b = map(int, input().split())
