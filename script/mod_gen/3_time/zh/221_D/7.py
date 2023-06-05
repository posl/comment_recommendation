def main():
    # 读入数据
    N = int(input())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append((A, B))
    # 计算答案
    D = [0] * (N + 1)
    for i in range(N):
        A, B = AB[i]
        D[A] += 1
        D[A + B] -= 1
    for i in range(N):
        D[i + 1] += D[i]
    # 输出答案
    print(*D[1:])

if __name__ == '__main__':
    main()