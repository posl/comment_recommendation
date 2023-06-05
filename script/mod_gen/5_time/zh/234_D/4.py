def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    p = P[:K]
    p.sort()
    print(p[-1])
    for i in range(N-K):
        p.remove(P[i])
        p.append(P[i+K])
        p.sort()
        print(p[-1])

if __name__ == '__main__':
    main()