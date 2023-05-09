def main():
    N, M = map(int, input().split())
    s = [0] * M
    c = [0] * M
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    for i in range(10 ** N):
        for j in range(M):
            if int(str(i)[s[j] - 1]) != c[j]:
                break
        else:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()