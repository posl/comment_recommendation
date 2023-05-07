def main():
    n = int(input())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(1,n-1):
        if p[i-1] == i-1 or p[i] == i or p[i+1] == i+1:
            ans += 1
    if p[0] == 0 or p[n-1] == n-1 or p[n-2] == n-2:
        ans += 1
    print(ans)
