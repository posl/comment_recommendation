def get_anagram_count(s):
    anagram_count = 0
    anagram_dict = {}
    for i in range(len(s)):
        s_sorted = ''.join(sorted(s[i]))
        if s_sorted in anagram_dict:
            anagram_count += anagram_dict[s_sorted]
            anagram_dict[s_sorted] += 1
        else:
            anagram_dict[s_sorted] = 1
    return anagram_count
