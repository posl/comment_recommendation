def main():
    n,q = map(int,input().split())
    follow = {}
    for i in range(1,n+1):
        follow[i] = []
    for i in range(q):
        t,a,b = map(int,input().split())
        if t == 1:
            follow[a].append(b)
        elif t == 2:
            follow[a].remove(b)
        elif t == 3:
            if b in follow[a] and a in follow[b]:
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    main()