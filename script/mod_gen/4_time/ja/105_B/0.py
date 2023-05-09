def solve():
    n = int(input())
    for i in range(0, n//4+1):
        for j in range(0, n//7+1):
            if 4*i + 7*j == n:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    solve()