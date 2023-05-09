def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort(reverse=True)
    ans = p[0] / 2
    for i in range(1, N):
        ans += p[i]
    print(int(ans))
