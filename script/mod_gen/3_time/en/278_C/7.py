def main():
    N, Q = map(int, input().split())
    follow = {}
    for i in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            if A not in follow:
                follow[A] = set()
            follow[A].add(B)
        elif T == 2:
            if A in follow:
                follow[A].discard(B)
        else:
            if A in follow and B in follow[A]:
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    main()