def main():
    # input
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    rcs = [[int(x) for x in input().split()] for _ in range(N)]
    Q = int(input())
    dls = [[x for x in input().split()] for _ in range(Q)]
    # compute
    # output
    print()

if __name__ == '__main__':
    main()