def main():
    S = input()
    for i in range(len(S)):
        if S[i] != S[len(S)-i-1]:
            print("No")
            return
    print("Yes")
