def main():
    N, M = map(int, input().split())
    # 1回目のマッチング
    match = []
    for i in range(1, 2*N, 2):
        match.append([i, i+1])
    # 2回目以降のマッチング
    for _ in range(M):
        A = input()
        match_new = []
        for i in range(N):
            if A[i] == 'G':
                if A[i+N] == 'P':
                    match_new.append(match[i][1])
                    match_new.append(match[i][0])
                elif A[i+N] == 'C':
                    match_new.append(match[i][0])
                    match_new.append(match[i][1])
                else:
                    match_new.append(match[i][0])
                    match_new.append(match[i][1])
            elif A[i] == 'C':
                if A[i+N] == 'P':
                    match_new.append(match[i][0])
                    match_new.append(match[i][1])
                elif A[i+N] == 'G':
                    match_new.append(match[i][1])
                    match_new.append(match[i][0])
                else:
                    match_new.append(match[i][0])
                    match_new.append(match[i][1])
            else:
                if A[i+N] == 'G':
                    match_new.append(match[i][0])
                    match_new.append(match[i][1])
                elif A[i+N] == 'C':
                    match_new.append(match[i][1])
                    match_new.append(match[i][0])
                else:
                    match_new.append(match[i][0])
                    match_new.append(match[i][1])
        match = match_new
    for i in range(2*N):
        print(match[i])

if __name__ == '__main__':
    main()