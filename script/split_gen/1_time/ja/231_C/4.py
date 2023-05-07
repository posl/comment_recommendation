def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for i in range(Q)]
    A.sort()
    for x in X:
        print(bisect.bisect_left(A, x))
