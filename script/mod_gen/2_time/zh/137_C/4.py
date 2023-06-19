def count_anagram(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    return count

if __name__ == '__main__':
    count_anagram()