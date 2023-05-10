def main():
    S = input()
    S = S.rstrip()
    S = S.lstrip()
    if len(S) == 1:
        print(0)
        return
    if len(S) == 2:
        if S[0] == S[1]:
            print(1)
            return
        else:
            print(0)
            return
    ret = 0
    for i in range(1,len(S)-1):
        if S[i-1] == S[i] and S[i] == S[i+1]:
            ret += 1
            if S[i] == '0':
                S = S[:i] + '1' + S[i+1:]
            else:
                S = S[:i] + '0' + S[i+1:]
    if S[0] == S[1]:
        ret += 1
    if S[len(S)-1] == S[len(S)-2]:
        ret += 1
    print(ret)

if __name__ == '__main__':
    main()