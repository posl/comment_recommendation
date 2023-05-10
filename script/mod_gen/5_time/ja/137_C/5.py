def get_anagram_count(s_list):
    anagram_count = 0
    anagram_dict = {}
    for s in s_list:
        s = ''.join(sorted(s))
        if s in anagram_dict:
            anagram_dict[s] += 1
        else:
            anagram_dict[s] = 1
    for key in anagram_dict.keys():
        if anagram_dict[key] > 1:
            anagram_count += anagram_dict[key] * (anagram_dict[key] - 1) // 2
    return anagram_count

if __name__ == '__main__':
    get_anagram_count()