def main():
    s = input()
    if s.count('o') + (15 - len(s)) >= 8:
        print('Yes')
    else:
        print('No')
