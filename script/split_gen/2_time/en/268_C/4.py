def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            ans += 1
            if i + 1 < N and p[i+1] == i + 1:
                p[i], p[i+1] = p[i+1], p[i]
    print(ans)
