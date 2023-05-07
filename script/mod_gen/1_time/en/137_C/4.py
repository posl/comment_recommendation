def count_anagrams(s):
    cnt = {}
    for c in s:
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1
    return cnt
n = int(input())
s = []
for i in range(n):
    s.append(input())
cnts = []
for i in range(n):
    cnts.append(count_anagrams(s[i]))
cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if cnts[i] == cnts[j]:
            cnt += 1
print(cnt)

if __name__ == '__main__':
    count_anagrams()