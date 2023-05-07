def main():
    #入力
    R,C = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(2)]
    #出力
    print(A[R-1][C-1])

if __name__ == '__main__':
    main()