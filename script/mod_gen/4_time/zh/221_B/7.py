def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        s = S[0:i] + S[i+1] + S[i] + S[i+2:]
        if s == T:
            print("Yes")
            return
    print("No")
    return
main()
