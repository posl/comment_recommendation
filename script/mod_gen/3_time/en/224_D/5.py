def main():
    M = int(input())
    edges = [list(map(int, input().split())) for _ in range(M)]
    pieces = list(map(int, input().split()))
    print(solve(edges, pieces))

if __name__ == '__main__':
    main()