def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        if S[:i] + S[i+1] + S[i] + S[i+2:] == T:
            print("Yes")
            return
    print("No")
    return
