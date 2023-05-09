def main():
    p = list(map(int, input().split()))
    s = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(26):
        print(s[p[i]-1], end='')
