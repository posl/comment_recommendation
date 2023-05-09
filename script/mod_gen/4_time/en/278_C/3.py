def main():
    n, q = map(int, input().split())
    follow = [set() for _ in range(n)]
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a-1].add(b-1)
        elif t == 2:
            follow[a-1].discard(b-1)
        else:
            if a-1 in follow[b-1] and b-1 in follow[a-1]:
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()