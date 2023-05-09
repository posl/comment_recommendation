def main():
    N,K = map(int,input().split())
    S = input()
    S = S.replace("RL","X")
    S = S.replace("LR","Y")
    S = S.replace("R","0")
    S = S.replace("L","1")
    S = S.replace("X","10")
    S = S.replace("Y","01")
    happy = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            happy += 1
    happy += min(2*K,2*N-2*happy-1)
    print(happy)

if __name__ == '__main__':
    main()