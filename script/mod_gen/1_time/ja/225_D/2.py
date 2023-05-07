def main():
    N,Q = map(int,input().split())
    train = [0] * (N+1)
    for i in range(1,N+1):
        train[i] = i
    for i in range(Q):
        c,x,y = map(int,input().split())
        if c == 1:
            train[x] = y
        elif c == 2:
            train[x] = x
        else:
            ans = [x]
            while train[x] != x:
                x = train[x]
                ans.append(x)
            print(len(ans),*ans)

if __name__ == '__main__':
    main()