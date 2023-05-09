def isHardToEnter(S):
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            return True
    return False

if __name__ == '__main__':
    isHardToEnter()