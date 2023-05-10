def main():
    #S = input()
    S = "023456789"
    #S = "459230781"
    S = list(S)
    S = [int(i) for i in S]
    S.sort()
    #print(S)
    #print(len(S))
    #print(S[0])
    #print(S[len(S)-1])
    #print(S[len(S)-1]-S[0])
    for i in range(1,len(S)):
        if S[i]-S[i-1] != 1:
            print(S[i-1]+1)
            break
    else:
        print(S[len(S)-1]+1)
    return
