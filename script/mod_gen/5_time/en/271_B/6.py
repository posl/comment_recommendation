def main():
    n, q = map(int, input().split())
    seq = []
    for i in range(n):
        seq.append(list(map(int, input().split())))
    query = []
    for j in range(q):
        query.append(list(map(int, input().split())))
    for k in range(q):
        print(seq[query[k][0]-1][query[k][1]-1])

if __name__ == '__main__':
    main()