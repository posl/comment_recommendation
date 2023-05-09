def main():
    S = input()
    K = int(input())
    #print(S)
    #print(K)
    #print(len(S))
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
    #Xを連続させる最大数を求める
    #Xの連続数を数える
    X_count = 0
    for i in range(len(S)):
        if S[i] == "X":
            X_count += 1
        else:
            break
    for i in range(len(S)-1, -1, -1):
        if S[i] == "X":
            X_count += 1
        else:
            break
    #print(X_count)
    #Xの連続数がSの長さと同じなら、Xを連続させる最大数はSの長さ
    if X_count == len(S):
        print(len(S))
        return
    #Xの連続数がSの長さと同じでないなら、Xを連続させる最大数はXの連続数+K
    else:
        print(X_count+K)

if __name__ == '__main__':
    main()