def main():
    s = input()
    s = list(map(int, s))
    s.reverse()
    print(s)
    ans = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if (s[i] + s[j] * 10) % 2019 == 0:
                ans += 1
    print(ans)
