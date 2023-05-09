def main():
    N, M = map(int,input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int,input().split())
    ans = 0
    for i in range(M):
        for j in range(i+1,M):
            if A[i] == A[j] or A[i] == B[j] or B[i] == A[j] or B[i] == B[j]:
                ans += 1
    print(ans)
