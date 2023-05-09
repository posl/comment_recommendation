def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    total = 0
    for i in range(N):
        if K > 0:
            if A[i] > X:
                total += X
                K -= 1
            else:
                total += A[i]
        else:
            total += A[i]
    print(total)
