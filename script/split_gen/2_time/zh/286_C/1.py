def solve():
    n, a, b = map(int, input().split())
    s = input()
    s = list(s)
    s1 = s[:n//2]
    s2 = s[n//2+1:]
    s2.reverse()
    ans = 0
    for i in range(n//2):
        if s1[i] != s2[i]:
            if s1[i] == 'a' and s2[i] == 'b':
                ans += a
            elif s1[i] == 'b' and s2[i] == 'a':
                ans += a
            elif s1[i] == 'c' and s2[i] == 'd':
                ans += a
            elif s1[i] == 'd' and s2[i] == 'c':
                ans += a
            elif s1[i] == 'e' and s2[i] == 'f':
                ans += a
            elif s1[i] == 'f' and s2[i] == 'e':
                ans += a
            elif s1[i] == 'g' and s2[i] == 'h':
                ans += a
            elif s1[i] == 'h' and s2[i] == 'g':
                ans += a
            elif s1[i] == 'i' and s2[i] == 'j':
                ans += a
            elif s1[i] == 'j' and s2[i] == 'i':
                ans += a
            elif s1[i] == 'k' and s2[i] == 'l':
                ans += a
            elif s1[i] == 'l' and s2[i] == 'k':
                ans += a
            elif s1[i] == 'm' and s2[i] == 'n':
                ans += a
            elif s1[i] == 'n' and s2[i] == 'm':
                ans += a
            elif s1[i] == 'o' and s2[i] == 'p':
                ans += a
            elif s1[i] == 'p' and s2[i] == 'o':
                ans += a
            elif s1[i] == 'q' and s2[i] == 'r':
                ans += a
            elif s1[i] == 'r' and s2
