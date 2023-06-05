def main():
    n, m = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(n)]
    A = [[(i-1)*7+j for j in range(1,8)] for i in range(1, 10**100+1)]
    for i in range(10**100-n+1):
        for j in range(7-m+1):
            if A[i][j:j+m] == B[0] and A[i+1][j:j+m] == B[1]:
                print("Yes")
                return
    print("No")
    return

if __name__ == '__main__':
    main()