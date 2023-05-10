def is_wonderful_string(s):
    if not any(c.isupper() for c in s):
        return False
    if not any(c.islower() for c in s):
        return False
    if len(set(s)) != len(s):
        return False
    return True
s = input()
print('Yes' if is_wonderful_string(s) else 'No')

if __name__ == '__main__':
    is_wonderful_string()