def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    else:
        for i in range(0,len(S)-1):
            if S[i] == T[i+1] and S[i+1] == T[i]:
                print("Yes")
                return
        print("No")
        return

if __name__ == '__main__':
    main()