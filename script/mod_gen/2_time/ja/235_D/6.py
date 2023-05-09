def main():
    a, n = map(int, input().split())
    if n == 1:
        print(0)
    else:
        print(bfs(a, n))

if __name__ == '__main__':
    main()