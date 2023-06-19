def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    #print(r,g,b)
    ans = r * g * b
    for i in range(n):
        for j in range(i+1,n):
            k = j + (j - i)
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[i] != s[k]:
                ans -= 1
    print(ans)
