def main():
    S = input()
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            print("Bad")
            return
    print("Good")
    return

if __name__ == '__main__':
    main()