def count_anagrams(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    return sum([v * (v - 1) // 2 for v in d.values()])
n = int(input())
s = [input() for _ in range(n)]
d = {}
for i in s:
    i = ''.join(sorted(i))
    d[i] = d.get(i, 0) + 1
print(sum([v * (v - 1) // 2 for v in d.values()]))

if __name__ == '__main__':
    count_anagrams()