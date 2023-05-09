def main():
    s = input()
    if s[0] == 'x':
        print(0)
    else:
        print(10**s.count('?'))
