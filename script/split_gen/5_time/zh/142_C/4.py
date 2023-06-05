def solve():
    # 读入
    N = int(input())
    # A = [int(input()) for i in range(N)]
    A = list(map(int, input().split()))
    # 数组B，用于记录A中的数是否已经被遍历过
    B = [False] * N
    # 数组C，用于记录学生进入教室的顺序
    C = [0] * N
    # 遍历A中的每个数
    for i in range(N):
        # 如果A[i]没有被遍历过
        if not B[A[i]-1]:
            # 将A[i]加入数组C
            C[i] = A[i]
            # 将A[i]标记为已经被遍历过
            B[A[i]-1] = True
        else:
            # 如果A[i]已经被遍历过，那么就从前往后遍历数组B，找到第一个没有被遍历过的数，将它加入数组C
            for j in range(N):
                if not B[j]:
                    C[i] = j + 1
                    B[j] = True
                    break
    # 打印数组C
    print(' '.join(map(str, C)))
solve()
