def check_concatenation(N, S):
    if N%2 != 0:
        return "No"
    else:
        if S[:N//2] == S[N//2:]:
            return "Yes"
        else:
            return "No"
N = int(input())
S = input()
print(check_concatenation(N, S))
