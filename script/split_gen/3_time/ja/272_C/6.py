def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = -1
    for i in range(n-1):
        if (a[i] + a[i+1]) % 2 == 0:
            ans = a[i] + a[i+1]
    print(ans)
