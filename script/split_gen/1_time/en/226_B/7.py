def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    #print(A)
    ans = N
    for i in range(N):
        for j in range(1, A[i][0]+1):
            if A[i][j] == 1:
                ans -= 1
                break
    print(ans)
main()
