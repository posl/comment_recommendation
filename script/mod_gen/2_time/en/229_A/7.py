def solve():
    S1 = input()
    S2 = input()
    if '#' in S1[0] and '#' in S2[0]:
        print('Yes')
    elif '#' in S1[1] and '#' in S2[1]:
        print('Yes')
    else:
        print('No')
solve()

if __name__ == '__main__':
    solve()