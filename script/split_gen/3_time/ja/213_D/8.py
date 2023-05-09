def main():
    N = int(input())
    # 都市の数
    A = []
    B = []
    # 都市の組み合わせ
    for i in range(N-1):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    # 都市1からの距離
    d = [0] * (N+1)
    # 旅のルート
    route = [1]
    # 都市1からの距離を計算
    for i in range(N-1):
        if A[i] == 1:
            d[B[i]] = 1
        elif B[i] == 1:
            d[A[i]] = 1
    # 旅のルートを計算
    for i in range(N-1):
        if d[A[i]] == 1 and d[B[i]] == 0:
            route.append(B[i])
            d[B[i]] = 1
        elif d[B[i]] == 1 and d[A[i]] == 0:
            route.append(A[i])
            d[A[i]] = 1
    route.append(1)
    for i in range(N-1):
        if d[A[i]] == 1 and d[B[i]] == 0:
            route.append(B[i])
            d[B[i]] = 1
        elif d[B[i]] == 1 and d[A[i]] == 0:
            route.append(A[i])
            d[A[i]] = 1
    for i in route:
        print(i,end=" ")
