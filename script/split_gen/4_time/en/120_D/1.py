def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = 0
    ans_list = [0] * M
    ans_list[M-1] = int(N*(N-1)/2)
    for i in range(M-1, 0, -1):
        if A[i] > B[i]:
            A[i], B[i] = B[i], A[i]
        if A[i] == 1:
            ans_list[i-1] = ans_list[i] - (N - B[i])*(N - B[i] - 1)/2
        else:
            ans_list[i-1] = ans_list[i] - (N - B[i])*(N - B[i] - 1)/2 + (A[i] - 1)*(A[i] - 2)/2
    for i in range(M):
        print(int(ans_list[i]))
