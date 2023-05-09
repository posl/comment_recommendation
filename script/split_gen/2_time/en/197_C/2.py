def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(30):
        c = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                c += 1
        ans += (1 << i) * (c * (n - c) % 2)
    print(ans)
