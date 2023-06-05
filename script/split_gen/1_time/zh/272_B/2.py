def main():
    N, M = map(int, input().split())
    k = []
    x = []
    for i in range(M):
        k.append(list(map(int, input().split())))
        x.append(k[i][1:])
    for i in range(N):
        for j in range(i + 1, N):
            flag = False
            for l in range(M):
                if i + 1 in x[l] and j + 1 in x[l]:
                    flag = True
            if not flag:
                print("No")
                return
    print("Yes")
    return
