def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        exit()
    for i in range(len(S)-1):
        if S[i] == T[i+1] and S[i+1] == T[i]:
            print("Yes")
            exit()
    print("No")
