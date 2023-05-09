def get_num_sequences(s, memo):
    if s < 3:
        return 0
    if s == 3:
        return 1
    if s in memo:
        return memo[s]
    num_sequences = 0
    for i in range(3, s - 1):
        num_sequences += get_num_sequences(s - i, memo)
    memo[s] = num_sequences
    return num_sequences

if __name__ == '__main__':
    get_num_sequences()