def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = t[i]
        for j in range(i, i + n):
            if ans[j % n] > ans[(j + 1) % n] + s[(j + 1) % n]:
                ans[j % n] = ans[(j + 1) % n] + s[(j + 1) % n]
    for i in range(n):
        print(ans[i])
