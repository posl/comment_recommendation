def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    good = 0
    for i in range(N):
        good += 1
        for j in range(M):
            if A[j] == i+1:
                if H[i] <= H[B[j]-1]:
                    good -= 1
                    break
            if B[j] == i+1:
                if H[i] <= H[A[j]-1]:
                    good -= 1
                    break
    print(good)
