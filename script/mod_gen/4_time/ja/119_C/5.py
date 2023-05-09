def main():
    n, a, b, c = map(int, input().split())
    ls = [int(input()) for _ in range(n)]
    print(bfs(n, a, b, c, ls))

if __name__ == '__main__':
    main()