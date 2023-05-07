def main():
    N, M = map(int, input().split())
    l = [i for i in range(1, M + 1)]
    for i in range(1, N + 1):
        for j in range(len(l) - 1, -1, -1):
            if l[j] <= l[-i]:
                l.pop(j)
    for i in range(len(l)):
        print(l[i], end = " ")
        for j in range(N - 1):
            print(l[i] + j + 1, end = " ")
        print("")

if __name__ == '__main__':
    main()