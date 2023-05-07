def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S)):
            S = S[-1] + S[:len(S)-1]
            if S == T:
                print("Yes")
                return
        print("No")

if __name__ == '__main__':
    main()