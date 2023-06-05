def main():
    N, M = map(int, input().split())
    n = [0] * M
    x = [0] * M
    for i in range(M):
        n[i], *x[i] = map(int, input().split())
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            for k in range(M):
                if i in x[k] and j in x[k]:
                    break
            else:
                print("No")
                exit()
    print("Yes")
main()
