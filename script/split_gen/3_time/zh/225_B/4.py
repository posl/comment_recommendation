def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N - 1):
        a, b = map(int, input().split())
        A[i] = a - 1
        B[i] = b - 1
    deg = [0] * N
    for i in range(N - 1):
        deg[A[i]] += 1
        deg[B[i]] += 1
    for i in range(N):
        if deg[i] == N - 1:
            print('Yes')
            return
    print('No')
main()
