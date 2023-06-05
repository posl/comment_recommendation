def count_alphabet(str_list):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_dict = {}
    for a in alphabet:
        alphabet_dict[a] = 0
    for str in str_list:
        for i in range(len(str)):
            alphabet_dict[str[i]] += 1
    count = 0
    for a in alphabet_dict:
        if alphabet_dict[a] == 2:
            count += 1
    return count

if __name__ == '__main__':
    count_alphabet()