def solve():
    S = input()
    if S[0] != 'A':
        print('WA')
        return
    if S[2:-1].count('C') != 1:
        print('WA')
        return
    for i in range(1,len(S)):
        if S[i] == 'C':
            continue
        if S[i].isupper():
            print('WA')
            return
    print('AC')

if __name__ == '__main__':
    solve()