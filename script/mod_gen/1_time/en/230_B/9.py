def is_substring(s):
    if 'o' not in s:
        return 'No'
    elif 'x' not in s:
        return 'Yes'
    elif 'x' not in s[0:s.find('o')]:
        return 'Yes'
    elif 'o' not in s[s.find('x'):]:
        return 'Yes'
    else:
        return 'No'
s = input()
print(is_substring(s))

if __name__ == '__main__':
    is_substring()