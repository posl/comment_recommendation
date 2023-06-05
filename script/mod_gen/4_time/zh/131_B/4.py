def solve():
    N,L = map(int, input().split())
    if N == 1:
        print(L)
        return
    if L >= 0:
        print(sum(range(L+1, L+N)))
        return
    if L+N-1 <= 0:
        print(sum(range(L, L+N-1)))
        return
    print((L+N-1)*N//2)
solve()
