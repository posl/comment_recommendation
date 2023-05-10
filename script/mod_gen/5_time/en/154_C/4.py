def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if len(A) == len(set(A)):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    solve()