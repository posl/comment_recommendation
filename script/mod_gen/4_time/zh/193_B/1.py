def solve():
    N = int(input())
    A_P_X = []
    for i in range(N):
        A_P_X.append(list(map(int, input().split())))
    A_P_X.sort(key=lambda x: x[0])
    min_price = float('inf')
    for i in range(N):
        if A_P_X[i][2] > 0:
            min_price = min(min_price, A_P_X[i][1])
    if min_price == float('inf'):
        print(-1)
    else:
        print(min_price)
solve()
