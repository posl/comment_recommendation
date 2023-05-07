def main():
    S = input()
    S = S + S
    S_min = S
    S_max = S
    for i in range(len(S)//2):
        if S[i:i+len(S)//2] < S_min:
            S_min = S[i:i+len(S)//2]
        if S[i:i+len(S)//2] > S_max:
            S_max = S[i:i+len(S)//2]
    print(S_min)
    print(S_max)
