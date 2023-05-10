def main():
    N, K = map(int, input().split())
    a = N
    for i in range(K):
        g1 = int("".join(sorted(str(a), reverse=True)))
        g2 = int("".join(sorted(str(a))))
        a = g1 - g2
    print(a)

if __name__ == '__main__':
    main()