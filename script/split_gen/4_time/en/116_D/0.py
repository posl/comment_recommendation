def main():
    N, K = map(int, input().split())
    T = [0] * N
    D = [0] * N
    for i in range(N):
        T[i], D[i] = map(int, input().split())
    T = [t-1 for t in T]
    ans = 0
    for s in range(2**N):
        if bin(s).count('1') != K:
            continue
        t = [0] * N
        for i in range(N):
            if s & (1 << i):
                t[T[i]] += 1
        t = sorted(t, reverse=True)
        x = 0
        for i in range(N):
            if t[i] > 0:
                x += 1
            else:
                break
        total = 0
        for i in range(N):
            if s & (1 << i):
                total += D[i]
        ans = max(ans, total + x*x)
    print(ans)
