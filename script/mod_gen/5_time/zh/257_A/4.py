def problems257_a():
    n, x = map(int, input().split())
    s = ''
    for i in range(26):
        s += chr(65+i) * n
    print(s[x-1])

if __name__ == '__main__':
    problems257_a()