def get_anagram_count(s):
    s = sorted(s)
    count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
    return count
