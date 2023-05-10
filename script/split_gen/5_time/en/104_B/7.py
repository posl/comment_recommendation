def main():
    s = input()
    if s[0] == 'A' and s[2:-1].count('C') == 1:
        for i in range(1, len(s)):
            if s[i] != 'C' and s[i].isupper():
                print("WA")
                exit()
        print("AC")
    else:
        print("WA")
