def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    for i in range(w):
        s[i] = ''.join([s[j][i] for j in range(h)])
        t[i] = ''.join([t[j][i] for j in range(h)])
    s.sort()
    t.sort()
    print('Yes' if s == t else 'No')

if __name__ == '__main__':
    main()