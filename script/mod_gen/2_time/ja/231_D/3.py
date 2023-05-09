def main():
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        edge[A-1].append(B-1)
        edge[B-1].append(A-1)
    ans = "Yes"
    for i in range(N):
        for j in edge[i]:
            for k in edge[j]:
                if i in edge[k]:
                    ans = "No"
                    break
    print(ans)

if __name__ == '__main__':
    main()