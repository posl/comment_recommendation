def count_anagram(s):
    from collections import Counter
    count = Counter(s)
    return count

if __name__ == '__main__':
    count_anagram()