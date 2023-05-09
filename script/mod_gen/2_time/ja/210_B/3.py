def main():
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == '1':
            if (i+1) % 2 == 0:
                print("Aoki")
            else:
                print("Takahashi")
            return

if __name__ == '__main__':
    main()