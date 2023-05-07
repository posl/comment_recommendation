def main():
    from collections import Counter
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    
    c = Counter()
    for i in range(N):
        for j in range(i + 1, N):
            c[(x[i] + x[j], y[i] + y[j])] += 1
    
    ans = 0
    for k, v in c.items():
        ans += v * (v - 1) // 2
    
    print(ans)
