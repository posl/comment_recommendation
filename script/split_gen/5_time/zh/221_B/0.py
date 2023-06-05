def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        if S[i:i+2] == T[i+1:i-1:-1]:
            print("Yes")
            return
    print("No")
    return
