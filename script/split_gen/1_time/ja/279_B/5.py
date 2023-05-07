def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-len(T)):
        if S[i:i+len(T)] == T:
            print("Yes")
            return
    print("No")
    return
