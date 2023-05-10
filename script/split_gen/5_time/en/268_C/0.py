def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            ans += 1
            if i < N-1 and p[i+1] == i+1:
                p[i], p[i+1] = p[i+1], p[i]
            elif i == N-1:
                p[i], p[0] = p[0], p[i]
    print(ans)
