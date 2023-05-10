def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    #print(S)
    max = 0
    cnt = 0
    for i in range(1,N):
        if S[i-1] == S[i]:
            cnt += 1
            if cnt > max:
                max = cnt
        else:
            cnt = 0
    #print(max)
    cnt = 0
    for i in range(1,N):
        if S[i-1] == S[i]:
            cnt += 1
            if cnt == max:
                print(S[i])
        else:
            cnt = 0
