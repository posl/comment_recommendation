def find_num_of_sequences(S):
    # 递归
    if S <= 2:
        return 0
    if S == 3:
        return 1
    if S == 4:
        return 2
    return find_num_of_sequences(S - 3) + find_num_of_sequences(S - 4)

if __name__ == '__main__':
    find_num_of_sequences()