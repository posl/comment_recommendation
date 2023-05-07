def main():
    L, Q = map(int, input().split())
    queries = []
    for _ in range(Q):
        c, x = map(int, input().split())
        queries.append((c, x))
    print(queries)

if __name__ == '__main__':
    main()