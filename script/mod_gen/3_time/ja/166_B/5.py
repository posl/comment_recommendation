def main():
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(int(input()))
        a = []
        for j in range(d[i]):
            a.append(int(input()))
        print(a)

if __name__ == '__main__':
    main()