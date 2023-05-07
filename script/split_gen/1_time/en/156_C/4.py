def main():
    N = int(input())
    X = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(1, 101):
        s = 0
        for j in X:
            s += (i - j) ** 2
        ans = min(ans, s)
    print(ans)
