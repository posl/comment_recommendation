def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S)-1):
            if S[i] != S[i+1]:
                S = S[:i] + S[i+1] + S[i] + S[i+2:]
                break
        if S == T:
            print("Yes")
        else:
            print("No")
