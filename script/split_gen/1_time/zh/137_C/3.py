def count_anagrams(arr):
    anagrams = {}
    for s in arr:
        key = ''.join(sorted(s))
        if key in anagrams:
            anagrams[key] += 1
        else:
            anagrams[key] = 1
    count = 0
    for key in anagrams:
        n = anagrams[key]
        count += n * (n-1) / 2
    return count
