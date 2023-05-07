def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        exit()
    p = list(map(int, input().split()))
    p.sort()
    p.append(1000)
    ans = 1000
    for i in range(1, n + 1):
        if p[i] - p[i - 1] > 1:
            for j in range(p[i - 1] + 1, p[i]):
                if abs(x - j) < abs(x - ans):
                    ans = j
    print(ans)
