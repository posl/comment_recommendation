def solve():
    # 写下你的代码
    S = input()
    if S[-1] == 's':
        print(S + 'es')
    else:
        print(S + 's')

if __name__ == '__main__':
    solve()