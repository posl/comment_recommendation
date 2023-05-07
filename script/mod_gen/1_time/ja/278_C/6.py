def main():
    N,Q = map(int,input().split())
    follow = [set() for _ in range(N)]
    for _ in range(Q):
        t,a,b = map(int,input().split())
        if t == 1:
            follow[a-1].add(b-1)
        elif t == 2:
            follow[b-1].add(a-1)
        else:
            if a-1 in follow[b-1]:
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()