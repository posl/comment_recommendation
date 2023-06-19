def main():
    S = input()
    S = S * 2
    S_min = S[0:len(S)//2]
    S_max = S[0:len(S)//2]
    for i in range(1, len(S)//2):
        S_tmp = S[i:i+len(S)//2]
        if S_tmp < S_min:
            S_min = S_tmp
        if S_tmp > S_max:
            S_max = S_tmp
    print(S_min)
    print(S_max)
