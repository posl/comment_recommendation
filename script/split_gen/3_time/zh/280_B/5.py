def main():
    #输入
    N = int(input())
    S = list(map(int, input().split()))
    #求和
    sum = 0
    for i in range(N):
        sum += S[i]
    #求A
    A = [0] * N
    A[0] = sum // N
    for i in range(1, N):
        A[i] = 2 * S[i - 1] - A[i - 1]
    #输出
    for i in range(N):
        print(A[i], end=' ')
