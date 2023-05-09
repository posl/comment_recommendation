def get_anagram_count(str1, str2):
    return (sorted(str1) == sorted(str2))

if __name__ == '__main__':
    get_anagram_count()