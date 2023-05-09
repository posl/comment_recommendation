def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(list(input()))
    #print(S)
    # horizontal
    for i in range(N):
        cnt = 0
        for j in range(N):
            if S[i][j] == "#":
                cnt = 0
            else:
                cnt += 1
                if cnt >= 6:
                    print("Yes")
                    return
    # vertical
    for i in range(N):
        cnt = 0
        for j in range(N):
            if S[j][i] == "#":
                cnt = 0
            else:
                cnt += 1
                if cnt >= 6:
                    print("Yes")
                    return
    # diagonal
    for i in range(N):
        cnt = 0
        for j in range(N):
            if i+j < N:
                if S[i+j][j] == "#":
                    cnt = 0
                else:
                    cnt += 1
                    if cnt >= 6:
                        print("Yes")
                        return
            else:
                break
    for i in range(N):
        cnt = 0
        for j in range(N):
            if i+j < N:
                if S[j][i+j] == "#":
                    cnt = 0
                else:
                    cnt += 1
                    if cnt >= 6:
                        print("Yes")
                        return
            else:
                break
    print("No")
