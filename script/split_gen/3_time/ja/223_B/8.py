def main():
    S = input()
    S = list(S)
    S_min = S
    S_max = S
    for i in range(len(S)):
        S.append(S.pop(0))
        if S < S_min:
            S_min = S
        if S > S_max:
            S_max = S
        S = list(S)
    print(''.join(S_min))
    print(''.join(S_max))
