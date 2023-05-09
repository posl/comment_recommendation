def main():
    s = 'abcdefghijklmnopqrstuvwxyz'
    p = list(map(int, input().split()))
    for i in range(len(p)):
        print(s[p[i] - 1], end='')
