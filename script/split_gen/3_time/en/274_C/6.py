def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = a[::-1]
    ans = [0] * (2**n+1)
    for i in range(n):
        ans[a[i]] = ans[a[i]*2] + 1
        ans[a[i]*2+1] = ans[a[i]*2] + 1
    print(*ans[1:], sep='
')
