def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = [0] * 200
    for i in range(n):
        count[a[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += count[i] * (count[i] - 1) // 2
    print(ans)
