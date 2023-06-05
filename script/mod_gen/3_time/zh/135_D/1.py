def count13(s):
    if len(s) == 0:
        return 0
    if s[0] == '?':
        return (3 * count13(s[1:]) + count13(s[1:])) % (10**9 + 7)
    else:
        return count13(s[1:])

if __name__ == '__main__':
    count13()