def solve(n,s):
    r = s.count("R")
    g = s.count("G")
    b = s.count("B")
    ans = r * g * b
    for i in range(n):
        for j in range(1,n):
            k = 2 * j - i
            if k < n and k > j:
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                    ans -= 1
    return ans
n = int(input())
s = input()
print(solve(n,s))
