def solve():
    S = input()
    N = len(S)
    if N % 2 == 1:
        print('No')
        return
    l = 0
    for i in range(N):
        if S[i] == '(':
            l += 1
        elif S[i] == ')':
            l -= 1
        else:
            if l == 0:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    solve()