def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))
    # compute
    B = [0] * (N+1)
    for i in range(N):
        if A[i] < N+1:
            B[A[i]] += 1
    # print(B)
    # output
    for i in range(N+1):
        if B[i] == 0:
            print(i)
            exit()
