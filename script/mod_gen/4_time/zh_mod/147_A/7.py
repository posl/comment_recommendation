def solve():
    a = list(map(int, input().split()))
    if sum(a) >= 22:
        print('bust')
    else:
        print('win')

if __name__ == '__main__':
    solve()