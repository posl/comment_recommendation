def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
        return
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    print("Yes" if len(set(sum(edges, ()))) == N else "No")

if __name__ == '__main__':
    main()