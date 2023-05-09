def main():
    N,M = map(int,input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i],B[i] = map(int,input().split())
    ans = "Yes"
    for i in range(M):
        for j in range(M):
            if A[i] == B[j]:
                ans = "No"
    print(ans)
