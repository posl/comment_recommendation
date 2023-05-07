def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i]:
                    if A[i] < A[j] < A[k] or A[k] < A[j] < A[i]:
                        cnt += 1
    print(cnt)
