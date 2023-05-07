def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    K = []
    for i in range(Q):
        x, k = map(int, input().split())
        X.append(x)
        K.append(k)
    # リストの中のxの出現回数を数える
    # それをリストで返す
    def count_x(A, x):
        count = 0
        count_x = []
        for i in range(len(A)):
            if A[i] == x:
                count += 1
            count_x.append(count)
        return count_x
    # リストの中のxの出現回数を数える
    # それを辞書で返す
    def count_x2(A, x):
        count = 0
        count_x = {}
        for i in range(len(A)):
            if A[i] == x:
                count += 1
            count_x[A[i]] = count
        return count_x
    # リストの中のxの出現回数を数える
    # それを辞書で返す
    # ただし、リストの中のxの最初の出現回数は0とする
    def count_x3(A, x):
        count = 0
        count_x = {}
        for i in range(len(A)):
            if A[i] == x:
                count += 1
            count_x[A[i]] = count
        count_x[x] = 0
        return count_x
    # リストの中のxの出現回数を数える
    # それを辞書で返す
    # ただし、リストの中のxの最初の出現回数は0とする
    # また、リストの中のxの最後の出現回数はリストの長さとする
    def count_x4(A, x):
        count = 0
        count_x = {}
        for i in range(len(A)):
            if A[i] == x:
                count += 1
            count_x[A[i]] =
