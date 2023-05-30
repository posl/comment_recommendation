def main():
    S = input()
    S_min = S
    S_max = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S < S_min:
            S_min = S
        if S > S_max:
            S_max = S
    print(S_min)
    print(S_max)
main()
