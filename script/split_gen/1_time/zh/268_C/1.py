def main():
    N = int(input())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    p.insert(N+1, 0)
    ans = 0
    for i in range(1, N+1):
        if (p[i-1] < p[i] < p[i+1]) or (p[i+1] < p[i] < p[i-1]):
            ans += 1
    print(ans)
