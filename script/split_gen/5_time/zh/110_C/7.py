def main():
    S = input()
    T = input()
    S = list(S)
    T = list(T)
    if S == T:
        print("Yes")
    else:
        for i in range(len(S)-1):
            S[i],S[i+1] = S[i+1],S[i]
            if S == T:
                print("Yes")
                break
            else:
                S[i], S[i + 1] = S[i + 1], S[i]
        else:
            print("No")
