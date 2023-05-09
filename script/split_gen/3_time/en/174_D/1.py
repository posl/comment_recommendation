def main():
    n = int(input())
    s = input()
    w = s.count('W')
    r = s.count('R')
    if w == 0 or r == 0:
        print(0)
    else:
        ans = 0
        for i in range(w):
            if s[i] == 'R':
                ans += 1
        print(ans)
