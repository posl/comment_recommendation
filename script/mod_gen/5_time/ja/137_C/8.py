def count_word(word):
    cnt = [0] * 26
    for c in word:
        cnt[ord(c) - ord('a')] += 1
    return tuple(cnt)
n = int(input())
cnt = {}
for _ in range(n):
    word = input()
    c = count_word(word)
    if c in cnt:
        cnt[c] += 1
    else:
        cnt[c] = 1
ans = 0
for v in cnt.values():
    ans += v * (v - 1) // 2
print(ans)

if __name__ == '__main__':
    count_word()