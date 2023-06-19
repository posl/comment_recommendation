def main():
    L,Q = map(int,input().split())
    mark = [False for i in range(L+1)]
    mark[0] = True
    mark[L] = True
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            mark[x] = True
        else:
            for i in range(x):
                if mark[x-i] == True:
                    left = x-i
                    break
            for i in range(x,L+1):
                if mark[i] == True:
                    right = i
                    break
            print(right-left)

if __name__ == '__main__':
    main()