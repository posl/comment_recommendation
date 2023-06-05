def main():
    N, M = map(int, input().split())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(M):
        T.append(input())
    #print(N)
    #print(M)
    #print(S)
    #print(T)
    count = 0
    for i in range(M):
        for j in range(N):
            if T[i] == S[j]:
                count += 1
                break
    print(count)

if __name__ == '__main__':
    main()