def main():
    N, M = map(int, input().split())
    s = []
    c = []
    for _ in range(M):
        s_, c_ = map(int, input().split())
        s.append(s_)
        c.append(c_)
    if N == 1 and M == 0:
        print(0)
        return
    if M == 0:
        print(10**(N-1))
        return
    if N > 1:
        if 1 not in s:
            s.append(1)
            c.append(1)
    for i in range(10**(N-1), 10**N):
        for j in range(M):
            if int(str(i)[s[j]-1]) != c[j]:
                break
        else:
            print(i)
            return
    print(-1)
    return

if __name__ == '__main__':
    main()