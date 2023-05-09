def main():
    S = input()
    K = int(input())
    cnt = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            cnt += 1
    ans = min(cnt+2*K,len(S)-1)
    print(ans)

if __name__ == '__main__':
    main()