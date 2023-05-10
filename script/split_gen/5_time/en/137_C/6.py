def get_anagram_count(s):
    anagram_count = 0
    anagram_dict = {}
    for i in range(len(s)):
        sorted_s = ''.join(sorted(s[i]))
        if sorted_s in anagram_dict:
            anagram_count += anagram_dict[sorted_s]
            anagram_dict[sorted_s] += 1
        else:
            anagram_dict[sorted_s] = 1
    return anagram_count
