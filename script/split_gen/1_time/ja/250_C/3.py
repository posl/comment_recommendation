def main():
    N, Q = map(int, input().split())
    A = [i for i in range(1, N+1)]
    for i in range(Q):
        x = int(input())
        A[x-1], A[x] = A[x], A[x-1]
    print(*A)
