def main():
    N = int(input())
    p = []
    for _ in range(N):
        p.append(int(input()))
    p.sort(reverse=True)
    ans = p[0] / 2
    for i in range(1, N):
        ans += p[i]
    print(int(ans))
