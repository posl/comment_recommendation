def main():
    N,M = map(int,input().split())
    A_B = [list(map(int,input().split())) for _ in range(N)]
    A_B.sort()
    ans = 0
    for i in range(N):
        if M > A_B[i][1]:
            ans += A_B[i][0]*A_B[i][1]
            M -= A_B[i][1]
        else:
            ans += A_B[i][0]*M
            break
    print(ans)
