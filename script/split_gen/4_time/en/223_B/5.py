def main():
    S = input()
    T = S
    for i in range(len(S)):
        S = S[-1] + S[:-1]
        if S < T:
            T = S
    print(T)
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S > T:
            T = S
    print(T)
