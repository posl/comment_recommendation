def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            if i == 0:
                p[i+1], p[i] = p[i], p[i+1]
            elif i == N-1:
                p[i-1], p[i] = p[i], p[i-1]
            else:
                p[i+1], p[i] = p[i], p[i+1]
            ans += 1
    print(ans)
