def move(S):
    ans = ""
    for i in range(len(S)-1):
        ans += S[i]
    ans += "0"
    return ans
S = input()
print(move(S))
