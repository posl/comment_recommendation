def main():
    N, X = map(int, input().split())
    alist = []
    blist = []
    for i in range(N):
        a, b = map(int, input().split())
        alist.append(a)
        blist.append(b)
    for i in range(N):
        if X - alist[i] >= 0:
            X -= alist[i]
        elif X - blist[i] >= 0:
            X -= blist[i]
        else:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()