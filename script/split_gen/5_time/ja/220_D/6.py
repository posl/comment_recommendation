def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * 10
    ans[a[0]] = 1
    for i in range(n-1):
        ans2 = [0] * 10
        for j in range(10):
            ans2[(j+a[i+1])%10] += ans[j]
            ans2[(j*a[i+1])%10] += ans[j]
        ans = ans2
    for i in range(10):
        print(ans[i]%998244353)
