def main():
    # 读入数据
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Query = []
    for i in range(Q):
        Query.append(list(map(int, input().split())))
    # 处理
    for i in range(Q):
        L, R, X = Query[i][0], Query[i][1], Query[i][2]
        count = 0
        for j in range(L-1, R):
            if A[j] == X:
                count += 1
        print(count)
