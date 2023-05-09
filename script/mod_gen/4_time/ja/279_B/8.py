def check(S,T):
    if len(S)<len(T):
        return False
    for i in range(len(S)-len(T)+1):
        if S[i:i+len(T)]==T:
            return True
    return False
S=input()
T=input()

if __name__ == '__main__':
    check()