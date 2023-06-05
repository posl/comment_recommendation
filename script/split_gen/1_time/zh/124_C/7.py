def solve():
    s = input()
    s = s.replace("01", "0 1").replace("10", "1 0").split()
    print(min(len(s[::2]), len(s[1::2])))
