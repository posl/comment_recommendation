def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    # 順列のリストを作る
    def permutation(N):
        if N == 1:
            return [[1]]
        else:
            A = permutation(N-1)
            B = []
            for a in A:
                for i in range(N):
                    b = list(a)
                    b.insert(i, N)
                    B.append(b)
            return B
    # 辞書順で何番目かを返す
    def dic_number(N, A):
        if N == 1:
            return 1
        else:
            a = A[0]
            A = A[1:]
            return (a-1) * math.factorial(N-1) + dic_number(N-1, A)
    # 辞書順で何番目かを返す
    def dic_number2(N, A):
        if N == 1:
            return 1
        else:
            a = A[0]
            A = A[1:]
            return (a-1) * math.factorial(N-1) + dic_number(N-1, A)
    # 辞書順で何番目かを返す
    def dic_number3(N, A):
        if N == 1:
            return 1
        else:
            a = A[0]
            A = A[1:]
            return (a-1) * math.factorial(N-1) + dic_number(N-1, A)
    # 辞書順で何番目かを返す
    def dic_number4(N, A):
        if N == 1:
            return 1
        else:
            a = A[0]
            A = A[1:]
            return (a-1) * math.factorial(N-1) + dic_number(N-1, A)
    # 辞書順で何番目かを返す
    def dic_number5(N, A):
        if N == 1:
            return 1
        else:
            a = A[0]
            A = A[1:]
            return (a-1) * math.factorial(N-1)
