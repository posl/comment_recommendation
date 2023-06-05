def main():
    N, M = map(int, input().split())
    k = []
    x = []
    for i in range(M):
        k.append(list(map(int, input().split())))
        x.append(k[i][1:])
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                flag = True
                for l in range(M):
                    if i + 1 not in x[l] or j + 1 not in x[l]:
                        flag = False
                if flag:
                    print("Yes")
                    exit()
    print("No")

if __name__ == '__main__':
    main()