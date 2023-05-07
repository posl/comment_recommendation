def main():
    # 1. input
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    
    # 2. create graph
    G = [[0] * N for _ in range(N)]
    for a, b in AB:
        G[a-1][b-1] = 1
        G[b-1][a-1] = 1
    
    # 3. search
    ans = 0
    for i in range(3**N):
        # 3.1. check condition
        flag = True
        for j in range(N):
            for k in range(j+1, N):
                if G[j][k] == 1 and (i//3**j)%3 == (i//3**k)%3:
                    flag = False
                    break
            if not flag:
                break
        # 3.2. count
        if flag:
            ans += 1
    print(ans)
