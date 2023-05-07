def main():
    s = input()
    k = int(input())
    n = len(s)
    if k == 0:
        print(max(map(len, s.split('.'))))
        return
    if n == 1:
        print(1)
        return
    if s[0] == 'X':
        s = '.' + s
    if s[-1] == 'X':
        s = s + '.'
    s = s.replace('X', '.')
    s = s.replace('..', '.')
    if s[0] == '.':
        s = s[1:]
    if s[-1] == '.':
        s = s[:-1]
    if len(s) == 0:
        print(0)
        return
    if k >= len(s):
        print(len(s))
        return
    s = s.split('.')
    if k == len(s):
        print(sum(map(len, s)) + k - 1)
        return
    if k < len(s):
        print(sum(map(len, s[:k + 1])) + k)
        return

if __name__ == '__main__':
    main()