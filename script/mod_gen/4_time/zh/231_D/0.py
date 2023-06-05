def main():
    # 读取输入
    N, M = map(int, input().split())
    A, B = [], []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 计算每个人的入度
    in_degrees = [0] * (N + 1)
    for i in range(M):
        in_degrees[B[i]] += 1
    # 计算拓扑排序的结果
    result = []
    queue = []
    for i in range(1, N + 1):
        if in_degrees[i] == 0:
            queue.append(i)
    while len(queue) > 0:
        v = queue.pop(0)
        result.append(v)
        for i in range(M):
            if A[i] == v:
                in_degrees[B[i]] -= 1
                if in_degrees[B[i]] == 0:
                    queue.append(B[i])
    # 检查是否有环
    if len(result) != N:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()