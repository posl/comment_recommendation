def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    total = sum(a)
    if k >= n:
        print(0)
    else:
        print(total - sum(a[-k:]))
