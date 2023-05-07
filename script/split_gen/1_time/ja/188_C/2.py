def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(2**i):
            if a[2*j] > a[2*j+1]:
                a[j] = a[2*j]
            else:
                a[j] = a[2*j+1]
                ans += 2**i
    print(ans+1)
