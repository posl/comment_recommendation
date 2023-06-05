def countAC(S):
    count = 0
    for i in range(len(S)-1):
        if S[i]+S[i+1] == 'AC':
            count += 1
    return count

if __name__ == '__main__':
    countAC()