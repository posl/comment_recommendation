def main():
    S = input()
    S = S[:1000]
    min = S
    max = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S < min:
            min = S
        elif S > max:
            max = S
    print(min)
    print(max)
