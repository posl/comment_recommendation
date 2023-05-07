def main():
    n, q = map(int, input().split())
    # 1: follow, 2: unfollow
    t, a, b = [0]*q, [0]*q, [0]*q
    for i in range(q):
        t[i], a[i], b[i] = map(int, input().split())
    # 1: follow, 2: unfollow
    for i in range(q):
        if t[i] == 1:
            print('follow')
        elif t[i] == 2:
            print('unfollow')
        else:
            print('check')

if __name__ == '__main__':
    main()