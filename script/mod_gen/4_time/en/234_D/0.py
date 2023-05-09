def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(N-K+1):
        print(sorted(P[i:i+K])[-1])

if __name__ == '__main__':
    main()