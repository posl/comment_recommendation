def main():
    N, M = map(int, input().split())
    s = [0] * M
    c = [0] * M
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    for i in range(10 ** N):
        i = str(i)
        if len(i) == N:
            for j in range(M):
                if i[s[j] - 1] != str(c[j]):
                    break
            else:
                print(i)
                exit()
    print(-1)
main()

if __name__ == '__main__':
    main()