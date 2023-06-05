def main():
    # 读取数据
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    # 穷举
    min_cost = float('inf')
    for i in range(2 ** N):
        cost = 0
        understand = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if all(x >= X for x in understand):
            min_cost = min(min_cost, cost)
    if min_cost == float('inf'):
        print(-1)
    else:
        print(min_cost)
