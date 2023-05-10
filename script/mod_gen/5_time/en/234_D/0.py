def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = []
    for i in range(N-K+1):
        ans.append(sorted(P[i:i+K])[-1])
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()