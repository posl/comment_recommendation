def anagram(s):
    return ''.join(sorted(s))
n = int(input())
d = {}
for _ in range(n):
    s = input()
    anagram_s = anagram(s)
    if anagram_s not in d:
        d[anagram_s] = 0
    d[anagram_s] += 1
print(sum(v * (v - 1) // 2 for v in d.values()))

if __name__ == '__main__':
    anagram()