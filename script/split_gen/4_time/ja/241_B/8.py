def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    cnt = 0
    for i in range(M):
        for j in range(cnt,N):
            if A[j] >= B[i]:
                cnt += 1
                break
    if cnt >= M:
        print("Yes")
    else:
        print("No")
