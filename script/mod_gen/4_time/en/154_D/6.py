def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    #print(N, K, p)
    #print([sum(p[i:i+K]) for i in range(N-K+1)])
    print(max([sum(p[i:i+K]) for i in range(N-K+1)]) / 2 + K / 2)

if __name__ == '__main__':
    main()