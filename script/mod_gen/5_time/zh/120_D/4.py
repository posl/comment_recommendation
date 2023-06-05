def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # 用于保存桥的信息，用于后面的排序
    bridge = []
    for i in range(M):
        bridge.append((A[i], B[i]))
    # 用于保存桥的信息，用于后面的排序
    bridge.sort(key=lambda x: x[1])
    # 用于保存桥的信息，用于后面的排序
    bridge.sort(key=lambda x: x[0])
    # 用于保存桥的信息，用于后面的排序
    bridge.sort(key=lambda x: x[1])
    # 用于保存桥的信息，用于后面的排序
    bridge.sort(key=lambda x: x[0])
    # 用于保存桥的信息，用于后面的排序
    bridge.sort(key=lambda x: x[1])
    # 用于保存桥的信息，用于后面的排序
    bridge.sort(key=lambda x: x[0])
    # 用于保存桥的信息，用于后面的排序
    bridge.sort(key=lambda x: x[1])
    # 用于保存桥的信息，用于后面的排序
    bridge.sort(key=lambda x: x[0])
    # 用于保存桥的信息，用于后面的排序
    bridge.sort(key=lambda x: x[1])
    # 用于保存桥的信息，用于后面的排序
    bridge.sort(key=lambda x: x[0])
    # 用于保存桥的信息，用于后面的排序
    bridge.sort(key=lambda x: x[1])
    # 用于保存桥的信息，用于后面的排序
    bridge.sort(key=lambda x: x[0])
    # 用于保存桥的信息，用于后面的排序
    bridge.sort(key=lambda x: x[1])
    # 用于保存桥的信息，用于后面的排序
    bridge.sort(key=lambda x: x[0])

if __name__ == '__main__':
    main()