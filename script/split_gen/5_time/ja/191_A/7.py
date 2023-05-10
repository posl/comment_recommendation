def solve():
    V, T, S, D = list(map(int, input().split()))
    if (T*V <= D) and (D <= S*V):
        print('No')
    else:
        print('Yes')
