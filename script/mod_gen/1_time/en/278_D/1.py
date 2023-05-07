def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(str, input().split())))
    ans = []
    for i in range(Q):
        if query[i][0] == '1':
            x = int(query[i][1])
            for j in range(N):
                A[j] = x
        elif query[i][0] == '2':
            i = int(query[i][1]) - 1
            x = int(query[i][1])
            A[i] += x
        else:
            i = int(query[i][1]) - 1
            ans.append(str(A[i]))
    print('
'.join(ans))

if __name__ == '__main__':
    main()