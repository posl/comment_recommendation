def solve():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(-1)
        return
    if N == 1:
        if X == A:
            print(0)
        else:
            print(-1)
        return
    if (X-A)%D != 0:
        print(-1)
        return
    n = (X-A)//D + 1
    if n < 1:
        print(-1)
        return
    if n > N:
        print(-1)
        return
    print(N-n)
    return

if __name__ == '__main__':
    solve()