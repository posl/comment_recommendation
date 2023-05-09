def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
    for i in range(1000):
        if len(str(i)) != N:
            continue
        flag = True
        for j in range(M):
            if int(str(i)[S[j] - 1]) != C[j]:
                flag = False
                break
        if flag:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()