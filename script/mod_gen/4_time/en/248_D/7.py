def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    ans = []
    for query in queries:
        ans.append(len([i for i in A[query[0]-1:query[1]] if i==query[2]]))
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()