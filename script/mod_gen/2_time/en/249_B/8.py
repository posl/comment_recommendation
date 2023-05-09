def is_wonderful_string(s):
    return "Yes" if len(set(s)) == len(s) and s.islower() and s.isupper() else "No"

if __name__ == '__main__':
    is_wonderful_string()