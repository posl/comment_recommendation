def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 中央値を求める関数
    def median(A):
        n = len(A)
        A.sort()
        if n % 2 == 0:
            return (A[n // 2 - 1] + A[n // 2]) / 2
        else:
            return A[n // 2]
    # mの中央値を求める
    M = []
    for i in range(N):
        for j in range(i, N):
            M.append(median(A[i:j + 1]))
    print(median(M))
