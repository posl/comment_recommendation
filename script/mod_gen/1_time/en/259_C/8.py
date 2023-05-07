def solve():
    S = input()
    T = input()
    #print(S)
    #print(T)
    S = S.replace('a', 'b')
    T = T.replace('a', 'b')
    #print(S)
    #print(T)
    if S == T:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    solve()