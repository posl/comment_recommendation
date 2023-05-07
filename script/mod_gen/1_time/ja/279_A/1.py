def main():
    S = input()
    ans = 0
    for i in range(len(S)-1):
        if S[i] == "v" and S[i+1] == "w":
            ans += 1
    print(ans*2)

if __name__ == '__main__':
    main()