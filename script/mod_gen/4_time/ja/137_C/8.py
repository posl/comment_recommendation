def count(s):
    res = 0
    for i in range(26):
        res += s[i]*(s[i]-1)//2
    return res
n = int(input())
ans = 0
s = [0]*26
for _ in range(n):
    t = input()
    s[ord(t[0])-ord('a')] += 1
    ans += count(s)
print(ans)

if __name__ == '__main__':
    count()