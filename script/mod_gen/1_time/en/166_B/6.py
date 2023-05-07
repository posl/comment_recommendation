def main():
    N, K = map(int, input().split())
    d = [0 for i in range(N)]
    for i in range(K):
        d_i = int(input())
        for j in range(d_i):
            d[int(input()) - 1] += 1
    print(d.count(0))

if __name__ == '__main__':
    main()