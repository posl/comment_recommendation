def main():
    N, M = map(int, input().split())
    a = []
    for i in range(M):
        a.append(list(map(int, input().split())))
    for i in range(M):
        for j in range(M):
            if i != j:
                for k in range(1, len(a[i])):
                    for l in range(1, len(a[j])):
                        if a[i][k] == a[j][l]:
                            print("Yes")
                            return
    print("No")

if __name__ == '__main__':
    main()