def main():
    N, M = map(int, input().split())
    #print(N, M)
    x = []
    for i in range(M):
        x.append(list(map(int, input().split())))
        #print(x[i])
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                flag = 0
                for k in range(M):
                    if i+1 in x[k] and j+1 in x[k]:
                        flag = 1
                        break
                if flag == 0:
                    print("No")
                    return
    print("Yes")
    return
