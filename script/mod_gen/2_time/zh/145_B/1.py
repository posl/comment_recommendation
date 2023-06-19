def solve():
    N = int(input())
    S = input()
    if N % 2 == 0 and S[:N//2] == S[N//2:]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    solve()