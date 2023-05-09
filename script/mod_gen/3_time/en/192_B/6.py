def hard_to_read(s):
    return all(s[i].islower() for i in range(0, len(s), 2)) and all(s[i].isupper() for i in range(1, len(s), 2))
s = input()

if __name__ == '__main__':
    hard_to_read()