def get_max_num_of_alphabets(N, K, S):
    max_num = 0
    for i in range(1, 2**N):
        i_str = str(bin(i))[2:]
        i_str = i_str.zfill(N)
        #print("i_str = {}".format(i_str))
        num_of_alphabets = 0
        for j in range(N):
            if i_str[j] == '1':
                num_of_alphabets += len(S[j])
        if num_of_alphabets == K:
            num_of_alphabets = 0
            alphabets = []
            for j in range(N):
                if i_str[j] == '1':
                    for k in range(len(S[j])):
                        if S[j][k] not in alphabets:
                            alphabets.append(S[j][k])
                            num_of_alphabets += 1
            if num_of_alphabets == K:
                max_num = max(max_num, i_str.count('1'))
    return max_num

if __name__ == '__main__':
    get_max_num_of_alphabets()