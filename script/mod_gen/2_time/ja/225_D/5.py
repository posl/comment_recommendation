def main():
    import sys
    input = sys.stdin.readline
    N,Q = map(int,input().split())
    A = [0]*N
    for i in range(N):
        A[i] = i
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            x,y = query[1],query[2]
            A[x-1] = y-1
        elif query[0] == 2:
            x,y = query[1],query[2]
            A[x-1] = x-1
        else:
            x = query[1]
            ans = []
            while True:
                ans.append(x)
                x = A[x-1]+1
                if x == 0:
                    break
            print(len(ans),*ans)
    return

if __name__ == '__main__':
    main()