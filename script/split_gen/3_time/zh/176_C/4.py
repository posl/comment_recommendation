def solve():
    N = int(input())
    A = list(map(int, input().split()))
    # print(N)
    # print(A)
    # 从最后一个人开始，往前看，如果比前一个人高，那么就把前一个人的高度加1
    # 如果比前一个人矮，那么就把前一个人的高度减到和当前人一样高
    # 这样一直到第一个人，就是最小的总高度
    # 注意，如果前一个人比当前人高，那么前一个人的高度减到和当前人一样高，那么前面的人也可能会变矮，所以要一直往前看
    height = 0
    for i in range(N - 1, 0, -1):
        if A[i] > A[i - 1]:
            height += A[i] - A[i - 1]
        elif A[i] < A[i - 1]:
            A[i - 1] = A[i]
    print(height)
