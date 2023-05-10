def main():
    H, W, rs, cs = map(int, input().split())
    N = int(input())
    rc = []
    for i in range(N):
        rc.append(list(map(int, input().split())))
    Q = int(input())
    dl = []
    for i in range(Q):
        dl.append(list(input().split())))
    print(H, W, rs, cs)
    print(N)
    print(rc)
    print(Q)
    print(dl)

if __name__ == '__main__':
    main()