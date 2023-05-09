def main():
    N, M = map(int, input().split())
    if M == 0:
        print("Yes")
        return
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    CD = [tuple(map(int, input().split())) for _ in range(M)]
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(M):
                if AB[k][0] == i + 1 and AB[k][1] == j + 1:
                    AB[k] = (i, j)
                elif AB[k][0] == j + 1 and AB[k][1] == i + 1:
                    AB[k] = (j, i)
                if CD[k][0] == i + 1 and CD[k][1] == j + 1:
                    CD[k] = (i, j)
                elif CD[k][0] == j + 1 and CD[k][1] == i + 1:
                    CD[k] = (j, i)
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(N):
                for l in range(k + 1, N):
                    for m in range(M):
                        if AB[m][0] == i and AB[m][1] == j and CD[m][0] == k and CD[m][1] == l:
                            break
                    else:
                        print("No")
                        return
    print("Yes")
    return
