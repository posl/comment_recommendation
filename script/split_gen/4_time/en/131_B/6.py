def main():
    n, l = map(int, input().split())
    if l >= 0:
        print((n-1)*l + (n*(n+1))//2 - (n-1))
    elif l < 0 and l+n-1 >= 0:
        print((n-1)*l + (n*(n+1))//2 - (n-1))
    else:
        print((n-1)*l + (n*(n+1))//2)
