def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S2 = []
    for i in range(N):
        if S[i] in S2:
            cnt = 1
            while True:
                if S[i] + '(' + str(cnt) + ')' in S2:
                    cnt += 1
                else:
                    S2.append(S[i] + '(' + str(cnt) + ')')
                    break
        else:
            S2.append(S[i])
    for i in range(N):
        print(S2[i])
