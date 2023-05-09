def main():
    N, Q = map(int, input().split())
    follow = [set() for _ in range(N)]
    for _ in range(Q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            follow[a].add(b)
        elif t == 2:
            follow[b].add(a)
        else:
            if a in follow[b]:
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    main()