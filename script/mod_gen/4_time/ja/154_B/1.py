def replace_all(s, f, t):
    return s.replace(f, t)
s = input()
print(replace_all(s, s, 'x'))

if __name__ == '__main__':
    replace_all()