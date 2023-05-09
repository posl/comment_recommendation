def is_hard_to_read(s):
    for i in range(0, len(s), 2):
        if s[i] != s[i].upper():
            return 'No'
    for i in range(1, len(s), 2):
        if s[i] != s[i].lower():
            return 'No'
    return 'Yes'
s = input()
print(is_hard_to_read(s))

if __name__ == '__main__':
    is_hard_to_read()