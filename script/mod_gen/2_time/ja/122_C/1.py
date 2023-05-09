def main():
    N, Q = map(int, input().split())
    S = input()
    LR = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, Q)
    #print(S)
    #print(LR)
    #print("")
    #ACの数を数える
    count = 0
    for i in range(N-1):
        if S[i:i+2] == "AC":
            count += 1
    #print(count)
    #ACの数を数える
    for i in range(Q):
        l = LR[i][0]
        r = LR[i][1]
        #print(l, r)
        count = 0
        for j in range(l-1, r-1):
            if S[j:j+2] == "AC":
                count += 1
        print(count)

if __name__ == '__main__':
    main()