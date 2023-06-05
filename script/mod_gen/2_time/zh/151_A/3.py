def solve():
    c = input()
    if c == 'z':
        print('z')
    else:
        print(chr(ord(c) + 1))

if __name__ == '__main__':
    solve()