def main():
    R,C = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(2)]
    print(A[R-1][C-1])
main()
