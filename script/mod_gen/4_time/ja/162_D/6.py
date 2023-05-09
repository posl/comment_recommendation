def check(i,j,k):
    if s[i] != s[j] and s[i] != s[k] and s[j] != s[k] and j - i != k - j:
        return True
    else:
        return False
n = int(input())
s = list(input())
r = s.count("R")
g = s.count("G")
b = s.count("B")
ans = r * g * b
for i in range(n):
    for j in range(i+1,n):
        k = j + (j - i)
        if k < n and check(i,j,k):
            ans -= 1
print(ans)

if __name__ == '__main__':
    check()