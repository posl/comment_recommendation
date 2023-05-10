def main():
    S = input()
    K = int(input())
    S += 'X'
    cnt = 0
    for i in range(len(S)-1):
        if S[i] == 'X':
            cnt += 1
        else:
            if S[i+1] == 'X':
                cnt += 1
            else:
                if K > 0:
                    cnt += 1
                    K -= 1
    print(cnt)

if __name__ == '__main__':
    main()