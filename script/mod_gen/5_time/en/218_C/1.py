def match(S, T):
    for i in range(len(S)):
        for j in range(len(S)):
            if S[i][j] != T[i][j]:
                return False
    return True

if __name__ == '__main__':
    match()