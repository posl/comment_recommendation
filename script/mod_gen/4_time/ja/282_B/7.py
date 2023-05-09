def check(s1, s2):
    for i in range(len(s1)):
        if s1[i] == 'x' and s2[i] == 'x':
            return False
    return True
n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input())
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if check(s[i], s[j]):
            ans += 1
print(ans)

if __name__ == '__main__':
    check()