def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    count = 0
    for a in range(1, N-1):
        for b in range(a+1, N):
            for c in range(b+1, N+1):
                if [a, b] in edges and [b, c] in edges and [c, a] in edges:
                    count += 1
    print(count)
main()

if __name__ == '__main__':
    main()