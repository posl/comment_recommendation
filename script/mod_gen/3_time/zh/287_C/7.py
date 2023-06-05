def solve():
    N, M = map(int, input().split())
    u = [0] * M
    v = [0] * M
    for i in range(M):
        u[i], v[i] = map(int, input().split())
    # 1. 无向图
    for i in range(M):
        u[i] -= 1
        v[i] -= 1
    # 2. N个顶点
    if N != len(set(u + v)):
        print("No")
        return
    # 3. N-1条边
    if M != N - 1:
        print("No")
        return
    # 4. 一个序列
    if M != len(set(u + v)):
        print("No")
        return
    # 5. 1~N的排列组合
    if set(u + v) != set(range(N)):
        print("No")
        return
    # 6. 满足条件
    for i in range(M):
        if abs(u[i] - v[i]) != 1:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    solve()