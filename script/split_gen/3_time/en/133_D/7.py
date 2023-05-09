def main():
    N = int(input())
    A = list(map(int, input().split()))
    tmp = 0
    for i in range(N):
        tmp += (A[i] - A[(i+1)%N])
    print(2*tmp, end="")
    for i in range(1, N):
        print(" " + str(2*A[i-1] - tmp), end="")
        tmp = 2*A[i-1] - tmp
    print("")
