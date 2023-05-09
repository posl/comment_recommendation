def main():
    N, M = map(int, input().split())
    S_list = [input() for i in range(N)]
    T_list = [input() for i in range(M)]
    count = 0
    for i in range(N):
        for j in range(M):
            if S_list[i][-3:] == T_list[j]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()