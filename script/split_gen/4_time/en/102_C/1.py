def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - (i+1)
    b.sort()
    if n % 2 == 0:
        x = (b[n//2 - 1] + b[n//2]) // 2
    else:
        x = b[n//2]
    ans = 0
    for i in range(n):
        ans += abs(b[i] - x)
    print(ans)
