def main():
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(input())
        d.append(input())
    print(N - d.count("1"))

if __name__ == '__main__':
    main()