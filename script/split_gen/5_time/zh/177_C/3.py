def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    sum = 0
    for i in range(n):
        for j in range(i+1,n):
            sum += a[i]*a[j]
    print(sum%mod)
