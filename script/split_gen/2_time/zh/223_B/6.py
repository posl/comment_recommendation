def main():
    s = input()
    s_min = s
    s_max = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        s_min = min(s, s_min)
        s_max = max(s, s_max)
    print(s_min)
    print(s_max)
