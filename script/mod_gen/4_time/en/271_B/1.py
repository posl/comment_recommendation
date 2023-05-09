def main():
    n, q = map(int, input().split())
    seq = []
    for i in range(n):
        seq.append(list(map(int, input().split())))
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    for query in queries:
        print(seq[query[0]-1][query[1]-1])

if __name__ == '__main__':
    main()