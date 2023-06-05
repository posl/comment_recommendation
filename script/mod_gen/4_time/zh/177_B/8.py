def get_min_change_num(S, T):
    min_change_num = len(S)
    for i in range(len(S) - len(T) + 1):
        change_num = 0
        for j in range(len(T)):
            if S[i + j] != T[j]:
                change_num += 1
        if change_num < min_change_num:
            min_change_num = change_num
    return min_change_num

if __name__ == '__main__':
    get_min_change_num()