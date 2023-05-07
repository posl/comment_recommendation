def get_anagram_count(s_list):
    s_dict = {}
    count = 0
    for s in s_list:
        s_dict[s] = s_dict.get(s, 0) + 1
    for s in s_list:
        s_dict[s] -= 1
        for i in range(len(s)):
            s_dict[s[i + 1:] + s[:i + 1]] = s_dict.get(s[i + 1:] + s[:i + 1], 0) + 1
    for s in s_list:
        count += s_dict[s]
    return count

if __name__ == '__main__':
    get_anagram_count()