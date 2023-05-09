def main():
    N = int(input())
    p = [int(i) for i in input().split()]
    ans = 0
    for i in range(N):
        if p[i] == i:
            ans += 1
            if i < N-1:
                p[i], p[i+1] = p[i+1], p[i]
    print(ans)
