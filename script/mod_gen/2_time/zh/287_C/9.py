def main():
    N, M = map(int, input().split())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(M):
        T.append(input())
    count = 0
    for i in range(M):
        for j in range(N):
            if T[i] == S[j][3:6]:
                count += 1
                break
    print(count)

if __name__ == '__main__':
    main()