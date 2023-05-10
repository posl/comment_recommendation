def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
    #print(N, M, S, C)
    ans = -1
    for i in range(10 ** (N - 1), 10 ** N):
        for j in range(M):
            if int(str(i)[S[j] - 1]) != C[j]:
                break
        else:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    main()