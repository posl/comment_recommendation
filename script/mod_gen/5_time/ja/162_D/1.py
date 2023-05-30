def check(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            k = 2*j-i
            if k < len(s):
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                    if j-i != k-j:
                        count += 1
    return count
n = int(input())
s = input()
print(check(s))
