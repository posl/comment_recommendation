def main():
    N = int(input())
    S = [input() for _ in range(N)]
    # 6 or more consecutive squares painted black aligned vertically
    for s in S:
        if s.count('#') >= 6:
            print('Yes')
            return
    # 6 or more consecutive squares painted black aligned horizontally
    for i in range(N):
        cnt = 0
        for j in range(N):
            if S[j][i] == '#':
                cnt = 0
            else:
                cnt += 1
                if cnt >= 6:
                    print('Yes')
                    return
    # 6 or more consecutive squares painted black aligned diagonally
    for i in range(N - 5):
        for j in range(N - 5):
            cnt = 0
            for k in range(6):
                if S[i + k][j + k] == '#':
                    cnt = 0
                else:
                    cnt += 1
                    if cnt >= 6:
                        print('Yes')
                        return
    for i in range(N - 5):
        for j in range(5, N):
            cnt = 0
            for k in range(6):
                if S[i + k][j - k] == '#':
                    cnt = 0
                else:
                    cnt += 1
                    if cnt >= 6:
                        print('Yes')
                        return
    print('No')
main()

if __name__ == '__main__':
    main()