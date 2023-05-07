def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
        return
    if len(S) < len(T):
        print('No')
        return
    for i in range(len(S)-len(T)+1):
        if S[i:i+len(T)] == T:
            print('Yes')
            return
    print('No')
