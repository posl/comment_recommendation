def coffee_like(s):
    if s[2] == s[3] and s[4] == s[5]:
        return True
    else:
        return False
s = input()

if __name__ == '__main__':
    coffee_like()