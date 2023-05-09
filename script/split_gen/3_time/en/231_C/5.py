def main():
    #input
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    #solve
    A.sort()
    for x in X:
        print(N - bisect.bisect_right(A, x))
