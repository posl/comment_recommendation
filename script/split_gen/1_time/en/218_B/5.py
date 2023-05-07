def main():
    p = input().split()
    s = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(26):
        print(s[int(p[i])-1], end='')
    print()
