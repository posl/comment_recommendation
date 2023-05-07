def count_anagram_pairs(strings):
    anagram_count = 0
    anagram_dict = {}
    for string in strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagram_dict:
            anagram_count += anagram_dict[sorted_string]
            anagram_dict[sorted_string] += 1
        else:
            anagram_dict[sorted_string] = 1
    return anagram_count
