def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    # 使い方
    # A = [1, 2, 3, 4, 5]
    # B = [1, 3, 5]
    # C = [10, 30, 50]
    # print(replace(A, B, C))
    # [10, 2, 30, 4, 50]
    def replace(A, B, C):
        for i in range(len(B)):
            for j in range(len(A)):
                if A[j] == B[i]:
                    A[j] = C[i]
        return A
    # 使い方
    # A = [1, 2, 3, 4, 5]
    # B = [1, 3, 5]
    # C = [10, 30, 50]
    # print(replace_sum(A, B, C))
    # 110
    def replace_sum(A, B, C):
        sum = 0
        for i in range(len(B)):
            for j in range(len(A)):
                if A[j] == B[i]:
                    A[j] = C[i]
        for i in range(len(A)):
            sum += A[i]
        return sum
    for i in range(Q):
        print(replace_sum(A, B, C))

if __name__ == '__main__':
    main()