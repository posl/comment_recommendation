def main():
    n = int(input())
    s = input()
    r_num = s.count('R')
    g_num = s.count('G')
    b_num = s.count('B')
    ans = r_num * g_num * b_num
    for i in range(n-2):
        for j in range(i+1, n-1):
            k = 2 * j - i
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)
