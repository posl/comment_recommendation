def main():
    N = int(input())
    S = input()
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    s = S[:N]
    t = S[N:]
    flip = False
    for q in queries:
        if q[0] == 1:
            if q[1] <= N and q[2] <= N:
                if flip:
                    q[1] += N
                    q[2] += N
                s = swap(s, q[1]-1, q[2]-1)
            elif q[1] > N and q[2] > N:
                if not flip:
                    q[1] -= N
                    q[2] -= N
                t = swap(t, q[1]-1, q[2]-1)
            else:
                if not flip:
                    q[1] -= N
                    q[2] += N
                else:
                    q[1] += N
                    q[2] -= N
                s = swap(s, q[1]-1, q[2]-1)
        else:
            flip = not flip
    if flip:
        print(t+s)
    else:
        print(s+t)

if __name__ == '__main__':
    main()