def solve():
    N, M = map(int, input().split())
    if M == 0:
        print(3**N)
        return
    AB = [list(map(int, input().split())) for _ in range(M)]
    # print(AB)
    # print(N, M)
    # print(3**N)
    ans = 0
    for i in range(3**N):
        # print(i)
        flag = True
        for j in range(N):
            for k in range(j+1, N):
                # print(j, k)
                if i//(3**j)%3 == i//(3**k)%3:
                    for l in range(M):
                        if AB[l][0] == j+1 and AB[l][1] == k+1:
                            flag = False
                            break
                        if AB[l][0] == k+1 and AB[l][1] == j+1:
                            flag = False
                            break
        if flag:
            ans += 1
    print(ans)
    # print(3**N)

if __name__ == '__main__':
    solve()