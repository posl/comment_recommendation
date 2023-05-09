def solve():
    # implement process
    S = []
    for i in range(9):
        S.append(input())
    result = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                result += 1
    return result

if __name__ == '__main__':
    solve()