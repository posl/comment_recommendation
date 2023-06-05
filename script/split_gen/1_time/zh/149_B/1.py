def main():
    a,b,k = map(int,input().split())
    if a >= k:
        a = a - k
    elif a + b >= k:
        b = b - (k - a)
        a = 0
    else:
        a = 0
        b = 0
    print(a,b)
