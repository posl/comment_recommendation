def main():
    # input
    Q = int(input())
    queries = [input().split() for _ in range(Q)]
    # compute
    S = []
    ans = []
    for query in queries:
        if query[0] == '1':
            S.append(int(query[1]))
        elif query[0] == '2':
            num = int(query[1])
            c = min(int(query[2]), S.count(num))
            for _ in range(c):
                S.remove(num)
        else:
            ans.append(max(S) - min(S))
    # output
    for s in ans:
        print(s)

if __name__ == '__main__':
    main()