def solve():
    N = int(input())
    S = input()
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    # print(N, S, Q, query)
    first = S[:N]
    last = S[N:]
    for i in range(Q):
        if query[i][0] == 1:
            if query[i][1] <= N and query[i][2] <= N:
                first = first[:query[i][1] - 1] + last[query[i][2] - 1] + first[query[i][1]:]
                last = last[:query[i][2] - 1] + first[query[i][1] - 1] + last[query[i][2]:]
            elif query[i][1] <= N and query[i][2] > N:
                first = first[:query[i][1] - 1] + last[query[i][2] - 1 - N] + first[query[i][1]:]
                last = last[:query[i][2] - 1 - N] + first[query[i][1] - 1] + last[query[i][2] - N:]
            elif query[i][1] > N and query[i][2] <= N:
                first = first[:query[i][1] - 1 - N] + last[query[i][2] - 1] + first[query[i][1] - N:]
                last = last[:query[i][2] - 1] + first[query[i][1] - 1 - N] + last[query[i][2]:]
            else:
                first = first[:query[i][1] - 1 - N] + last[query[i][2] - 1 - N] + first[query[i][1] - N:]
                last = last[:query[i][2] - 1 - N] + first[query[i][1] - 1 - N] + last[query[i][2] - N:]
        else:
            first, last = last, first
    print(first + last)

if __name__ == '__main__':
    solve()