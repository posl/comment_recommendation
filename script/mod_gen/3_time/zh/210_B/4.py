def solve():
    n = int(input())
    s = input()
    if s[n-1] == '0':
        print('Takahashi')
    else:
        print('Aoki')

if __name__ == '__main__':
    solve()