def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - i
    b.sort()
    if n % 2 == 0:
        x = b[n//2-1]
        y = b[n//2]
        ans = y - x + 1
    else:
        ans = b[n//2] * 2 + 1
    print(ans)
