def solve():
    s = input()
    for i in range(len(s)):
        if (i % 2 == 1 and s[i] == 'L') or (i % 2 == 0 and s[i] == 'R'):
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    solve()