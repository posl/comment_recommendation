def main():
    N, M = map(int, input().split())
    if M == 0:
        if N == 1:
            print(0)
        else:
            print(10 ** (N - 1))
        return
    s = [0] * (N + 1)
    c = [0] * (N + 1)
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    if N == 1:
        if M == 1 and s[0] == 1:
            print(c[0])
        else:
            print(-1)
        return
    if M == 1:
        if s[0] == 1:
            if c[0] == 0:
                print(-1)
                return
            else:
                print(str(c[0]) + '0' * (N - 1))
                return
        else:
            print(str(c[0]) + '0' * (N - 2) + '1')
            return
    for i in range(M):
        if s[i] == 1 and c[i] == 0:
            print(-1)
            return
    for i in range(M):
        if s[i] == 1:
            print(str(c[i]) + '0' * (N - 1), end='')
            return
    print(-1)
    return
main()
