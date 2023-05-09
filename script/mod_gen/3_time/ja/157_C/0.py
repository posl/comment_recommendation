def main():
    N, M = map(int, input().split())
    s = [0] * M
    c = [0] * M
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    if N == 1:
        for i in range(M):
            if s[i] == 1 and c[i] == 0:
                print(-1)
                return
            else:
                print(c[i])
                return
    elif N == 2:
        for i in range(M):
            if s[i] == 1 and c[i] == 0:
                print(-1)
                return
        for i in range(10):
            for j in range(10):
                for k in range(M):
                    if s[k] == 1 and c[k] == i:
                        break
                    elif s[k] == 2 and c[k] == j:
                        break
                else:
                    print(i * 10 + j)
                    return
        print(-1)
    elif N == 3:
        for i in range(M):
            if s[i] == 1 and c[i] == 0:
                print(-1)
                return
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(M):
                        if s[l] == 1 and c[l] == i:
                            break
                        elif s[l] == 2 and c[l] == j:
                            break
                        elif s[l] == 3 and c[l] == k:
                            break
                    else:
                        print(i * 100 + j * 10 + k)
                        return
        print(-1)

if __name__ == '__main__':
    main()