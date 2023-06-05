def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [i + 1 - a[i] for i in range(n)]
    b.sort()
    if n % 2 == 1:
        ans = sum(b[n // 2 + 1:]) + sum(b[:n // 2])
    else:
        ans = sum(b[n // 2:]) + sum(b[:n // 2])
    print(ans)
