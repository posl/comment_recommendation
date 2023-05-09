def main():
    S = input()
    if S[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and S[-1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for i in range(1, len(S)-1):
            if S[i] in "0123456789":
                if i == len(S)-2:
                    print("Yes")
            else:
                print("No")
                break
    else:
        print("No")

if __name__ == '__main__':
    main()