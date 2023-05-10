def main():
    N, Q = map(int, input().split())
    follow = {}
    for i in range(1, N+1):
        follow[i] = set()
    for _ in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a].add(b)
        elif t == 2:
            follow[a].discard(b)
        else:
            if b in follow[a]:
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()