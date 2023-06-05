def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = set()
    ans = 0
    for i in range(n-k+1):
        b.add(a[i])
        if ans < len(b):
            ans = len(b)
        if ans == k:
            break
    print(ans)
