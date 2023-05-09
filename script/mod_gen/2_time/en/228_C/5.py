def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: sum(x), reverse=True)
    print("Yes" if sum(P[K-1]) > sum(P[K]) else "No")

if __name__ == '__main__':
    main()