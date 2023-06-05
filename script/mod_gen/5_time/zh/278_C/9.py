def main():
    N, Q = map(int, input().split())
    follow = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow.append([a, b])
        elif t == 2:
            follow.remove([a, b])
        else:
            if [a, b] in follow and [b, a] in follow:
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()