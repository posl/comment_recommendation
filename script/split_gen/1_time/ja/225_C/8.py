def main():
    #input
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    #compute
    A = [[(i-1)*M+j for j in range(1, M+1)] for i in range(1, N*M+1)]
    for i in range(N):
        if B[i] != A[i]:
            print("No")
            exit()
    print("Yes")
