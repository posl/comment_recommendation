def main():
    N, Q = map(int, input().split())
    follow = [set() for i in range(N)]
    for i in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            follow[A - 1].add(B - 1)
        elif T == 2:
            follow[A - 1].discard(B - 1)
        else:
            if A - 1 in follow[B - 1] and B - 1 in follow[A - 1]:
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()