def main():
    N = int(input())
    s = [input() for _ in range(N)]
    a = []
    for i in range(N):
        a.append(sorted([int(s[i][j]) for j in range(10)]))
    ans = 0
    for i in range(N):
        ans += sum(a[i][:3])
    print(ans)
