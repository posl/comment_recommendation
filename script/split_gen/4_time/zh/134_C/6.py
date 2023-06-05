def main():
    # N = int(input())
    # A = []
    # for i in range(N):
    #     A.append(int(input()))
    # for i in range(N):
    #     tmp = A[i]
    #     A[i] = 0
    #     print(max(A))
    #     A[i] = tmp
    # 以上是自己写的，但是会超时
    # 以下是参考答案
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    max_num = max(A)
    max_num2 = max(A[:A.index(max_num)] + A[A.index(max_num) + 1:])
    for i in range(N):
        if A[i] == max_num:
            print(max_num2)
        else:
            print(max_num)
