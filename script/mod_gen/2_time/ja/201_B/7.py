def main():
    N = int(input())
    S_T = []
    for i in range(N):
        S_T.append(input().split())
    T = []
    for i in range(N):
        T.append(int(S_T[i][1]))
    T.sort(reverse=True)
    for i in range(N):
        if int(S_T[i][1]) == T[1]:
            print(S_T[i][0])

if __name__ == '__main__':
    main()