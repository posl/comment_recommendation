def main():
    S = input()
    Smin = S
    Smax = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S < Smin:
            Smin = S
        if S > Smax:
            Smax = S
    print(Smin)
    print(Smax)

if __name__ == '__main__':
    main()