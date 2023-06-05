def main():
    n,q = map(int,input().split())
    follow = set()
    for i in range(q):
        t,a,b = map(int,input().split())
        if t == 1:
            follow.add((a,b))
        elif t == 2:
            follow.discard((a,b))
        else:
            if (a,b) in follow and (b,a) in follow:
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()