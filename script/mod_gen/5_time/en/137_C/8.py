def get_anagram_count(s):
    letter_count = [0] * 26
    for c in s:
        letter_count[ord(c) - ord('a')] += 1
    return tuple(letter_count)
N = int(input())
anagram_count = {}
for i in range(N):
    s = input()
    key = get_anagram_count(s)
    if key in anagram_count:
        anagram_count[key] += 1
    else:
        anagram_count[key] = 1
result = 0
for key in anagram_count:
    result += anagram_count[key] * (anagram_count[key] - 1) // 2
print(result)

if __name__ == '__main__':
    get_anagram_count()