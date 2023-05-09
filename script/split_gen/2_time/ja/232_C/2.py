def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(N):
                for l in range(k + 1, N):
                    flag = True
                    for a, b in AB:
                        if (a == i + 1 and b == j + 1) or (a == j + 1 and b == i + 1):
                            if not ((k + 1, l + 1) in CD or (l + 1, k + 1) in CD):
                                flag = False
                                break
                        elif (a == k + 1 and b == l + 1) or (a == l + 1 and b == k + 1):
                            if not ((i + 1, j + 1) in CD or (j + 1, i + 1) in CD):
                                flag = False
                                break
                    if flag:
                        print('Yes')
                        return
    print('No')
main()
