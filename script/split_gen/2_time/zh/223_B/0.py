def main():
    S = input()
    S = S + S
    S_min = S[0]
    S_max = S[0]
    for i in range(1,len(S)//2):
        if S[i:] < S_min:
            S_min = S[i:]
        if S[i:] > S_max:
            S_max = S[i:]
    print(S_min)
    print(S_max)
