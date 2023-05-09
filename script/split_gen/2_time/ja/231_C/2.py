def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for i in range(Q)]
    A.sort()
    for i in range(Q):
        print(N - bisect.bisect_left(A, x[i]))
