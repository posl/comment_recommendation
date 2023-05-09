def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    CD = [list(map(int, input().split())) for i in range(M)]
    for i in range(M):
        AB[i][0] -= 1
        AB[i][1] -= 1
        CD[i][0] -= 1
        CD[i][1] -= 1
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    if i == j or i == k or i == l or j == k or j == l or k == l:
                        continue
                    if AB[0][0] == i and AB[0][1] == j and CD[0][0] == k and CD[0][1] == l:
                        P = [i, j, k, l]
                        flag = 1
                        for m in range(M):
                            if AB[m][0] == P[AB[m][1]]:
                                if CD[m][0] == P[CD[m][1]]:
                                    continue
                                else:
                                    flag = 0
                                    break
                            else:
                                if CD[m][0] == P[CD[m][1]]:
                                    flag = 0
                                    break
                                else:
                                    continue
                        if flag == 1:
                            print("Yes")
                            exit()
    print("No")
