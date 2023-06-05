def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    s = sum(a)
    if n * m <= s:
        print(0)
    elif n * m - s <= k:
        print(n * m - s)
    else:
        print(-1)
