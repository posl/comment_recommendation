def main():
    import sys
    def input():
        return sys.stdin.readline()[:-1]
    N, K = list(map(int, input().split()))
    P = list(map(int, input().split()))
    for i in range(K, N):
        print(P[i-K])
    return
main()

if __name__ == '__main__':
    main()