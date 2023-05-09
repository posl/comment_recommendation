def main():
    N, M = map(int, input().split())
    p = [0] * (N+1)
    s = [0] * (N+1)
    for i in range(M):
        pi, si = input().split()
        pi = int(pi)
        if s[pi] == 0:
            s[pi] = si
            if si == "AC":
                p[pi] = 1
        else:
            if s[pi] == "AC":
                pass
            else:
                if si == "AC":
                    p[pi] = 1
                else:
                    pass
    print(sum(p), sum([p[i] * s[i] for i in range(1, N+1)]))

if __name__ == '__main__':
    main()