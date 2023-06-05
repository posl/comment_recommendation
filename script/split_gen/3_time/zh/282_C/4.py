def main():
    N = int(input())
    S = input()
    #print(N)
    #print(S)
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])
    #print(S[10])
    #print(S[11])
    #print(S[12])
    #print(S[13])
    #print(S[14])
    #print(S[15])
    #print(S[16])
    #print(S[17])
    #print(S[18])
    #print(S[19])
    for i in range(N):
        if S[i] == '"':
            if i % 2 == 0:
                print('"', end='')
            else:
                print('.', end='')
        else:
            print(S[i], end='')
