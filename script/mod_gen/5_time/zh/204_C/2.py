def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    #print(N, M, AB)
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i != j:
                flag = True
                for k in range(M):
                    if i == AB[k][0] and j == AB[k][1]:
                        flag = False
                if flag:
                    count += 1
    print(count)
main()
