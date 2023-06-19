def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if A[i] == 0 and A[j] == 0:
                continue
            if A[i] == 0 or A[j] == 0:
                continue
            if A[i] % A[j] == 0:
                cnt += 1
    print(cnt)
