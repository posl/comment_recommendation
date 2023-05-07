def main():
    S = input()
    #print(S)
    #print(len(S))
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    count = 0
    for i in range(0,len(S)-1):
        if S[i] == S[i+1]:
            count += 1
    print(count)
