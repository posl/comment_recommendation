def main():
    S = input()
    ans = 0
    for i in range(len(S)-1):
        if S[i] == "v" and S[i+1] == "v":
            ans += 1
        elif S[i] == "w" and S[i+1] == "w":
            ans += 1
    print(ans)
