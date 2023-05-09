def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))
    #print(S)
    #print(T)
    max_score = 0
    max_score_count = 0
    for i in range(N):
        if T[i] > max_score:
            max_score = T[i]
            max_score_count = 1
        elif T[i] == max_score:
            max_score_count += 1
    if max_score_count == 1:
        print(T.index(max_score) + 1)
    else:
        for i in range(N):
            if T[i] == max_score:
                for j in range(i):
                    if S[i] == S[j]:
                        max_score_count -= 1
                        break
        if max_score_count == 1:
            for i in range(N):
                if T[i] == max_score:
                    print(i + 1)
                    break
        else:
            for i in range(N):
                if T[i] == max_score:
                    for j in range(i):
                        if S[i] == S[j]:
                            print(j + 1)
                            break
                    break

if __name__ == '__main__':
    main()