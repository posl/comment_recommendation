def main():
    S = input()
    T = input()
    S = S.replace('?','a')
    T = T.replace('?','a')
    for i in range(0,len(S)-len(T)+1):
        if S[i:i+len(T)] == T:
            print('Yes')
        else:
            print('No')
