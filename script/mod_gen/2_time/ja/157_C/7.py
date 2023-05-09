def main():
    N, M = map(int, input().split())
    if N == 1 and M == 0:
        print(0)
        return
    if M == 0:
        print(10**(N-1))
        return
    s_c = []
    for i in range(M):
        s, c = map(int, input().split())
        s_c.append([s, c])
    s_c.sort()
    for i in range(M):
        if i == 0:
            if s_c[i][0] == 1 and s_c[i][1] == 0:
                print(-1)
                return
            else:
                num = s_c[i][1]
        else:
            if s_c[i][0] == s_c[i-1][0]:
                print(-1)
                return
            else:
                num += s_c[i][1] * 10**(s_c[i][0]-1)
    if len(str(num)) != N:
        print(-1)
        return
    print(num)

if __name__ == '__main__':
    main()