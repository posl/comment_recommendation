def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    result = 0
    for i in range(N-1):
        for j in range(i+1, N):
            result ^= A[i][j]
    print(result)
