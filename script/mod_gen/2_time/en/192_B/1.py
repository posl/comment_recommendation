def is_hard_to_read(s):
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i].isupper():
                return False
        else:
            if s[i].islower():
                return False
    return True
s = input()

if __name__ == '__main__':
    is_hard_to_read()