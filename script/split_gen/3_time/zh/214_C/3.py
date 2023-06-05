def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = t[i]
    for i in range(n):
        if ans[i] > ans[(i-1)%n] + s[(i-1)%n]:
            ans[i] = ans[(i-1)%n] + s[(i-1)%n]
    for i in range(n):
        print(ans[i])
