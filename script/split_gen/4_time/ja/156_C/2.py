def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    ans = 10 ** 9
    for i in range(x[0], x[-1] + 1):
        s = 0
        for j in x:
            s += (j - i) ** 2
        if s < ans:
            ans = s
    print(ans)
