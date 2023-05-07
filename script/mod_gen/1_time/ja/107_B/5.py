def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    #print(H, W)
    #print(S)
    #行ごとに処理
    for i in range(H):
        #print(S[i])
        if "#" in S[i]:
            #print("Yes")
            continue
        else:
            #print("No")
            S[i] = "."
    #列ごとに処理
    for i in range(W):
        #print(S[i])
        if "#" in S[i]:
            #print("Yes")
            continue
        else:
            #print("No")
            S[i] = "."
    #print(S)
    for i in range(H):
        print(S[i])

if __name__ == '__main__':
    main()