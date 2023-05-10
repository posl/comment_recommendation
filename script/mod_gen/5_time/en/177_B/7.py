def check(s,t):
    for i in range(len(s)-len(t)+1):
        if s[i:i+len(t)] == t:
            return True
    return False
s = input()
t = input()
ans = len(t)
for i in range(len(s)-len(t)+1):
    if check(s[i:i+len(t)],t):
        ans = min(ans,len(t)-sum([1 for j in range(len(t)) if s[i+j] == t[j]]))
print(ans)

if __name__ == '__main__':
    check()