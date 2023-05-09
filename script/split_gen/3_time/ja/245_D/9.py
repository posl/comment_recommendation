def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #Cの最高次の係数を割る
    a = C[-1]
    A = [a // A[-1] * ai for ai in A]
    C = [ai // A[-1] for ai in C]
    #Aをずらす
    A = [0] * (M + 1) + A
    #Bを計算
    B = [0] * (M + 1)
    for i in range(M + 1):
        B[i] = C[i] - sum([B[j] * A[i - j] for j in range(i)])
    print(*B)
