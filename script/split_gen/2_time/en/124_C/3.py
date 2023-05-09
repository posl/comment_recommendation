def main():
    S = input()
    if len(S) == 1:
        print(0)
        return
    ans = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            ans += 1
    print(ans)
