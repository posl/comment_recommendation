def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] + A[j] > max and (A[i] + A[j])%2 == 0:
                max = A[i] + A[j]
    if max == 0:
        print(-1)
    else:
        print(max)
