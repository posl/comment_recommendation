def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    ans = float("inf")
    for i in range(x[0], x[-1] + 1):
        tmp = 0
        for j in range(n):
            tmp += (x[j] - i) ** 2
        ans = min(ans, tmp)
    print(ans)
