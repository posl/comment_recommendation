def main():
    N,W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        for j in range(i,N):
            for k in range(j,N):
                if A[i] + A[j] + A[k] <= W:
                    count += 1
    print(count)
