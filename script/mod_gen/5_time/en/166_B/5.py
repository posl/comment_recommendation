def main():
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(list(map(int, input().split()))[1:])
    d = sum(d, [])
    print(N - len(set(d)))

if __name__ == '__main__':
    main()