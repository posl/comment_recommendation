def main():
    N = int(input())
    S = [0]*N
    T = [0]*N
    for i in range(N):
        S[i], T[i] = input().split()
        T[i] = int(T[i])
    S_set = set(S)
    S_set = sorted(S_set)
    S_set_num = len(S_set)
    S_set_index = [0]*S_set_num
    S_set_score = [0]*S_set_num
    S_set_score[0] = T[0]
    for i in range(1, N):
        if S[i] == S[i-1]:
            S_set_score[S_set_index[i-1]] = max(S_set_score[S_set_index[i-1]], T[i])
        else:
            S_set_index[i] = S_set_index[i-1] + 1
            S_set_score[S_set_index[i]] = T[i]
    max_score = max(S_set_score)
    for i in range(S_set_num):
        if S_set_score[i] == max_score:
            print(S.index(S_set[i])+1)
            break

if __name__ == '__main__':
    main()