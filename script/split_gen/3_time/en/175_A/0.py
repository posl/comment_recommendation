def main():
    s = input()
    if s[0] == s[1] == s[2] == 'R':
        print(3)
    elif s[0] == s[1] == 'R' or s[1] == s[2] == 'R':
        print(2)
    elif s[0] == 'R' or s[1] == 'R' or s[2] == 'R':
        print(1)
    else:
        print(0)
