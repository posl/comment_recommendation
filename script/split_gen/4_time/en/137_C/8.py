def anagram(s):
    s = sorted(s)
    return ''.join(s)
n = int(input())
s = []
for i in range(n):
    s.append(anagram(input()))
s = sorted(s)
ans = 0
cnt = 1
for i in range(1, n):
    if s[i-1] == s[i]:
        cnt += 1
    else:
        ans += cnt*(cnt-1)//2
        cnt = 1
ans += cnt*(cnt-1)//2
print(ans)
