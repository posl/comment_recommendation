def main():
    N, L = map(int, input().split())
    ans = sum([i+L-1 for i in range(1, N+1)])
    if L <= 0 <= L+N-1:
        print(ans)
    elif L+N-1 < 0:
        print(ans - (L+N-1))
    else:
        print(ans - L)
