def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    dic = {}
    for i in range(26):
        dic[x[i]] = chr(ord('a') + i)
    for i in range(n):
        s[i] = ''.join([dic[c] for c in s[i]])
    s.sort()
    for i in range(n):
        print(''.join([chr(ord('a') + x.index(c)) for c in s[i]]))

if __name__ == '__main__':
    main()