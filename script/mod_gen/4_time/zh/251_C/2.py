def get_best_score():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    # print(S)
    # print(T)
    best_score = 0
    best_score_index = 0
    for i in range(N):
        if T[i] > best_score:
            best_score = T[i]
            best_score_index = i
    # print(best_score_index)
    best_score_string = S[best_score_index]
    # print(best_score_string)
    best_score_index = 0
    for i in range(N):
        if S[i] == best_score_string:
            if T[i] == best_score:
                best_score_index = i
                break
    # print(best_score_index)
    print(best_score_index + 1)

if __name__ == '__main__':
    get_best_score()