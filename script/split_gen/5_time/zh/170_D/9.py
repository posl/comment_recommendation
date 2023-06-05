def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    cnt = 0
    for i in range(N):
        if i == 0:
            if A[i] != A[i+1]:
                cnt += 1
        elif i == N-1:
            if A[i] != A[i-1]:
                cnt += 1
        else:
            if A[i-1] != A[i] and A[i] != A[i+1]:
                cnt += 1
    print(cnt)
