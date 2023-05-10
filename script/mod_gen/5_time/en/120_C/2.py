def main():
    #input
    S = input()
    #compute
    cnt = 0
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            cnt += 1
    #output
    print(cnt)
    return 0

if __name__ == '__main__':
    main()