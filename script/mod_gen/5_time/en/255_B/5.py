def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for _ in range(N)]
    print(solve(N,K,A,XY))

if __name__ == '__main__':
    main()