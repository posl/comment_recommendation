def main():
    S = input()
    K = int(input())
    N = len(S)
    tmp = 0
    cnt = 0
    for i in range(N):
        if S[i] == "X":
            tmp += 1
        else:
            cnt += tmp*(tmp+1)//2
            tmp = 0
    cnt += tmp*(tmp+1)//2
    if K == 0:
        print(cnt)
        exit()
    if S[0] == "X":
        tmp = 1
    else:
        tmp = 0
    for i in range(1,N):
        if S[i] == "X":
            tmp += 1
        else:
            break
    if tmp > 0:
        cnt -= tmp*(tmp+1)//2
    if S[-1] == "X":
        tmp = 1
    else:
        tmp = 0
    for i in range(1,N):
        if S[-i-1] == "X":
            tmp += 1
        else:
            break
    if tmp > 0:
        cnt -= tmp*(tmp+1)//2
    for i in range(1,N-1):
        if S[i] == "X" and S[i-1] == "." and S[i+1] == ".":
            cnt -= 1
    print(cnt+K*2)

if __name__ == '__main__':
    main()