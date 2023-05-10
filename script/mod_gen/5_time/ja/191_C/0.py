def check(i, j, S):
    if S[i][j] == '.':
        return False
    if S[i+1][j] == '.':
        return False
    if S[i][j+1] == '.':
        return False
    if S[i+1][j+1] == '.':
        return False
    return True

if __name__ == '__main__':
    check()