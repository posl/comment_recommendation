def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    kill = 0
    for i in range(N):
        kill += min(A[i], B[i])
        B[i] -= min(A[i], B[i])
        kill += min(A[i+1], B[i])
        A[i+1] -= min(A[i+1], B[i])
    print(kill)
