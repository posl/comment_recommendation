def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    c = 0
    for i in range(N):
        for j in range(i,N):
            for k in range(j,N):
                if A[i] + A[j] + A[k] <= W:
                    c += 1
    print(c)
