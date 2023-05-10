def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Query = []
    for i in range(Q):
        Query.append(list(map(int, input().split())))
    ans = []
    for i in range(Q):
        ans.append(A[Query[i][0]-1:Query[i][1]].count(Query[i][2]))
    for i in range(Q):
        print(ans[i])
main()

if __name__ == '__main__':
    main()