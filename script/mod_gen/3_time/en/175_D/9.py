def main():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    C = list(map(int,input().split()))
    P = [p-1 for p in P]
    ans = -10**9
    for i in range(N):
        score = 0
        visited = [False]*N
        visited[i] = True
        score += C[i]
        j = P[i]
        while not visited[j]:
            visited[j] = True
            score += C[j]
            j = P[j]
        if score > 0:
            cycle = 0
            while not visited[j]:
                visited[j] = True
                cycle += C[j]
                j = P[j]
            m = K//(cycle//score)
            score = score*(m-1) + cycle*(m-1)*(m-2)//2 + score*(K-cycle//score*(m-1))
        ans = max(ans,score)
    print(ans)

if __name__ == '__main__':
    main()