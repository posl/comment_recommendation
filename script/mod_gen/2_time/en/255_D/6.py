def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    A.append(0)
    A.append(10**9)
    for x in X:
        s = 0
        t = 0
        for i in range(N+1):
            if A[i] <= x:
                s += A[i]
            else:
                t += A[i]
        print(t-s)
main()
