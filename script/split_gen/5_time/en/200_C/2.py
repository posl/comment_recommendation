def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 200
    for i in a:
        b[i % 200] += 1
    ans = 0
    for i in range(200):
        ans += b[i] * (b[i] - 1) // 2
    print(ans)
