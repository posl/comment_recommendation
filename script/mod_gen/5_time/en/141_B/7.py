def solve():
    S = input().rstrip()
    if all([S[i] in 'RUD' for i in range(0, len(S), 2)]) and all([S[i] in 'LUD' for i in range(1, len(S), 2)]):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    solve()