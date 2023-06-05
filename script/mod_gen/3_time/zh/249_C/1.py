def get_max_num_of_alphabets(N, K, S):
    max_num = 0
    for i in range(2**N):
        tmp = i
        tmp_num = 0
        alphabets = []
        while tmp > 0:
            if tmp % 2 == 1:
                alphabets.append(S[tmp_num])
            tmp_num += 1
            tmp = tmp >> 1
        if len(set(alphabets)) == K:
            max_num = max(max_num, len(set(alphabets)))
    return max_num

if __name__ == '__main__':
    get_max_num_of_alphabets()