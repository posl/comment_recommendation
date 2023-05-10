def check(s):
    if s.islower():
        return False
    if s.isupper():
        return False
    if s.isalpha():
        return True
s = input()

if __name__ == '__main__':
    check()