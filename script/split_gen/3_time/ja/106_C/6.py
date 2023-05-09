def main():
    S = input()
    K = int(input())
    #print(S,K)
    cnt = 0
    for i in range(len(S)):
        if S[i] == "1":
            cnt += 1
        else:
            break
    if cnt >= K:
        print(1)
    else:
        print(S[cnt])
