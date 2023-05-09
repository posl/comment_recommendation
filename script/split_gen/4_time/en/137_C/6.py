def count_anagrams(s):
    c = [0] * 26
    for i in range(10):
        c[ord(s[i]) - ord('a')] += 1
    return tuple(c)
N = int(input())
S = [input() for _ in range(N)]
from collections import Counter
c = Counter(count_anagrams(s) for s in S)
ans = 0
for v in c.values():
    ans += v * (v - 1) // 2
print(ans)
