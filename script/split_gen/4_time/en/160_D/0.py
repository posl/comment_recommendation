def main():
    n, x, y = map(int, input().split())
    ans = [0] * n
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            ans[min(j - i, abs(x - i) + 1 + abs(y - j))] += 1
    print(*ans[1:], sep='\n')
