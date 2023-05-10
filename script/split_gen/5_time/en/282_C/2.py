def main():
    n = int(input())
    s = input()
    s = s.split('"')
    for i in range(1, len(s), 2):
        s[i] = s[i].replace(',', '.')
    print('"'.join(s))
