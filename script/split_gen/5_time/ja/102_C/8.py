def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = 0
    for i in range(n):
        b += a[i] - (i+1)
    b = b // n
    ans = 0
    for i in range(n):
        ans += abs(a[i] - (b+i+1))
    print(ans)
