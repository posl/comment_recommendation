def main():
    n = int(input())
    a = list(map(int, input().split()))
    r = [0] * 200
    for i in range(n):
        r[a[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += r[i] * (r[i] - 1) // 2
    print(ans)
