def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    for k in K:
        x = 0
        for i in range(N):
            if A[i] <= x + k:
                k -= A[i] - x - 1
                x = A[i]
            else:
                print(x + k)
                break
        else:
            print(x + k)
