def solve():
    #read input
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    #check
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == 'W' and A[j][i] != 'L':
                return '不正确'
            if A[i][j] == 'L' and A[j][i] != 'W':
                return '不正确'
            if A[i][j] == 'D' and A[j][i] != 'D':
                return '不正确'
    return '正确'

if __name__ == '__main__':
    solve()