def main():
    S = input()
    T = input()
    ans = 1000
    for i in range(len(S)-len(T)+1):
        tmp = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                tmp += 1
        ans = min(ans,tmp)
    print(ans)

if __name__ == '__main__':
    main()