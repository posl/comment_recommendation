def main():
    S = input()
    ans = ""
    for i in range(0, len(S)-1):
        ans += S[i]
    ans += "0"
    print(ans)
