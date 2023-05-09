def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        S = S[-1] + S[0:-1]
        if S == T:
            print("Yes")
            return
    print("No")
