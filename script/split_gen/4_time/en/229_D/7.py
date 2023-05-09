def main():
    s = input()
    k = int(input())
    s = s.replace('.', 'X')
    if len(s) <= k:
        print(len(s))
    else:
        print(s[:k].count('X') + s[k:].count('X') + 1)
