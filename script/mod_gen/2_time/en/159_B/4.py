def strongPalindrome(S):
    if S == S[::-1]:
        if S[:(len(S)-1)//2] == S[:(len(S)-1)//2][::-1]:
            if S[(len(S)+3)//2-1:] == S[(len(S)+3)//2-1:][::-1]:
                return "Yes"
    return "No"
S = input()
print(strongPalindrome(S))
