def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    for i in range(N):
        P[i].append(P[i][0]+P[i][1]+P[i][2])
        ans.append(P[i][3])
    ans.sort(reverse=True)
    print("Yes" if ans.index(P[K-1][3]) < K else "No")

if __name__ == '__main__':
    main()