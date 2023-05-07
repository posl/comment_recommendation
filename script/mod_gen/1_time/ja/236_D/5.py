def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2*N-1)]
    #print(A)
    ans = 0
    for i in range(2*N-1):
        for j in range(i+1, 2*N):
            ans = ans ^ A[i][j-i-1]
    print(ans)

if __name__ == '__main__':
    main()