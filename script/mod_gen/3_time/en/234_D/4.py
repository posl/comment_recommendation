def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(K, N):
        print(max(P[i-K:i+1]))
main()

if __name__ == '__main__':
    main()