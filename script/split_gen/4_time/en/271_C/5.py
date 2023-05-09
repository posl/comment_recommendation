def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(1, n):
        a[i] += a[i-1]
        if a[i] >= 2*a[i-1]:
            ans = i
    print(ans+1)
