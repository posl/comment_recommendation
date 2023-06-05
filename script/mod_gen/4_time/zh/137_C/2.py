def count_anagrams(words):
    counts = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        counts[sorted_word] = counts.get(sorted_word, 0) + 1
    return sum(count * (count - 1) / 2 for count in counts.values())

if __name__ == '__main__':
    count_anagrams()