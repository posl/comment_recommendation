def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    d = {}
    for i in range(26):
        d[x[i]] = chr(ord('a') + i)
    for i in range(n):
        s[i] = ''.join([d[c] for c in s[i]])
    s.sort()
    for i in range(n):
        print(''.join([x[ord(c) - ord('a')] for c in s[i]]))

if __name__ == '__main__':
    main()