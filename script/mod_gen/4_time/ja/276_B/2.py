def main():
    n, m = map(int, input().split())
    path = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        path[a-1].append(b)
        path[b-1].append(a)
    for i in range(n):
        print(len(path[i]), *sorted(path[i]))

if __name__ == '__main__':
    main()