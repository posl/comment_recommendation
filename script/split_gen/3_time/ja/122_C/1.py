def main():
    N, Q = map(int, input().split())
    S = input()
    lr = [list(map(int, input().split())) for i in range(Q)]
    #print(N, Q)
    #print(S)
    #print(lr)
    #ACの個数を数える
    ac = [0] * (N + 1)
    for i in range(N):
        if S[i:i+2] == "AC":
            ac[i+1] = ac[i] + 1
        else:
            ac[i+1] = ac[i]
    for i in range(Q):
        print(ac[lr[i][1]-1] - ac[lr[i][0]-1])
