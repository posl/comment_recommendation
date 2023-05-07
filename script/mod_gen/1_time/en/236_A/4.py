def swap():
    s = input()
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    s = list(s)
    s[a], s[b] = s[b], s[a]
    s = ''.join(s)
    print(s)
swap()

if __name__ == '__main__':
    swap()