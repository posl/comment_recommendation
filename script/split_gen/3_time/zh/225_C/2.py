def main():
    n,m = map(int,input().split())
    B = [list(map(int,input().split())) for _ in range(n)]
    A = [[0 for _ in range(7)] for _ in range(100)]
    for i in range(100):
        for j in range(7):
            A[i][j] = (i)*7+j+1
    for i in range(100-n+1):
        for j in range(7-m+1):
            if A[i][j] == B[0][0]:
                for k in range(n):
                    for l in range(m):
                        if A[i+k][j+l] != B[k][l]:
                            break
                        if k == n-1 and l == m-1:
                            print("Yes")
                            exit()
    print("No")
