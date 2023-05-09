def main():
    N,X = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    for i in range(N):
        X -= a[i]
        if X < 0:
            print("No")
            return
        if i == N-1:
            X -= b[i]
            if X < 0:
                print("No")
                return
            else:
                print("Yes")
                return

if __name__ == '__main__':
    main()