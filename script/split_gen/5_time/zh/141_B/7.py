def main():
    s = input()
    s1 = s[0::2]
    s2 = s[1::2]
    if s1.count('R') == 0 and s1.count('U') == 0 and s1.count('D') == 0:
        print("Yes")
    else:
        print("No")
