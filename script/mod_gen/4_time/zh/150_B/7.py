def countABC(S):
    count = 0
    for i in range(0, len(S) - 2):
        if S[i] == 'A' and S[i + 1] == 'B' and S[i + 2] == 'C':
            count += 1
    return count

if __name__ == '__main__':
    countABC()