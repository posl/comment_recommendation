def get_hash(s):
    hash = [0]*26
    for i in range(10):
        hash[ord(s[i])-ord('a')] += 1
    return hash
n = int(input())
s = []
for i in range(n):
    s.append(input())
hash = []
for i in range(n):
    hash.append(get_hash(s[i]))
hash.sort()
ans = 0
cnt = 1
for i in range(n-1):
    if hash[i] == hash[i+1]:
        cnt += 1
    else:
        ans += cnt * (cnt-1) // 2
        cnt = 1
ans += cnt * (cnt-1) // 2
print(ans)
