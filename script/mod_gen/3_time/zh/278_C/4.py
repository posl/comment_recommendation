def main():
    N, Q = map(int, input().split())
    follow = set()
    follow_back = set()
    for i in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow.add((a, b))
        elif t == 2:
            follow_back.add((a, b))
        else:
            if (a, b) in follow and (b, a) in follow_back:
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()