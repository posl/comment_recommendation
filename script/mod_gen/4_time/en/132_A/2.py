def solve():
    S = input()
    if len(set(S)) == 2:
        if S.count(S[0]) == 2 and S.count(S[1]) == 2:
            print('Yes')
            return
    print('No')
    return

if __name__ == '__main__':
    solve()