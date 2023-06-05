def get_max_num_of_letters_in_K_strings(N, K, S):
    max_num_of_letters = 0
    for i in range(1, 2**N):
        num_of_letters = 0
        letters = set()
        for j in range(N):
            if (i >> j) & 1:
                num_of_letters += len(S[j])
                letters = letters.union(set(S[j]))
        if num_of_letters == K and len(letters) == K:
            max_num_of_letters = K
            break
        elif num_of_letters > max_num_of_letters and len(letters) == K:
            max_num_of_letters = num_of_letters
    return max_num_of_letters

if __name__ == '__main__':
    get_max_num_of_letters_in_K_strings()