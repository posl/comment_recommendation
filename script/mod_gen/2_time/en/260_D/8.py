def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [-1 for _ in range(N)]
    #print(N, K, P)
    #print(ans)
    table = []
    for i, p in enumerate(P):
        table.append(p)
        while len(table) >= K:
            #print(table)
            if table[-K] == min(table[-K:]):
                for j in range(K):
                    ans[table.pop() - 1] = i + 1
            else:
                break
    print('
'.join(map(str, ans)))
main()

if __name__ == '__main__':
    main()