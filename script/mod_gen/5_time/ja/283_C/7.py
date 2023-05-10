def main():
    # input
    S = input()
    # compute
    cnt = 0
    for i in range(len(S)-1):
        if S[i] == '0':
            cnt += 1
    if S[-1] == '0':
        cnt += 1
    else:
        cnt += int(S[-1])
    # output
    print(cnt)

if __name__ == '__main__':
    main()