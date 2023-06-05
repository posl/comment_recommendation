def main():
    N, Q = map(int, input().split())
    follow = {}
    followed = {}
    for i in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow.setdefault(a, set()).add(b)
            followed.setdefault(b, set()).add(a)
        elif t == 2:
            follow.setdefault(a, set()).discard(b)
            followed.setdefault(b, set()).discard(a)
        elif t == 3:
            if follow.get(a, set()) & followed.get(b, set()):
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    main()