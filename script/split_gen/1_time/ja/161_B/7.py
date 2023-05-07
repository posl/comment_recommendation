def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    sumA = sum(A)
    cnt = 0
    for i in range(M):
        if A[i] < (sumA/(4*M)):
            break
        else:
            cnt += 1
    if cnt == M:
        print("Yes")
    else:
        print("No")
