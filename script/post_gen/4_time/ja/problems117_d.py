Synthesizing 1/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    # print(A)
    # print(N, K)

    # Kの最大値は10^12なので、2進数で40桁ぐらい
    # 2進数で最大40桁の1を��
