def swap(S, T):
    for i in range(len(S)-1):
        if S[i] != T[i]:
            if S[i+1] != T[i+1]:
                return False
    return True
S = input()
T = input()

if __name__ == '__main__':
    swap()