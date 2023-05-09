def is_wonderful_string(s):
    return 'Yes' if s.lower() != s and s.upper() != s and len(s) == len(set(s)) else 'No'
s = input()
print(is_wonderful_string(s))

if __name__ == '__main__':
    is_wonderful_string()