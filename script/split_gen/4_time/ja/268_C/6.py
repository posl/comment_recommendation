def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            if i == N-1:
                p[0], p[i] = p[i], p[0]
            else:
                p[i+1], p[i] = p[i], p[i+1]
            ans += 1
    print(ans)
