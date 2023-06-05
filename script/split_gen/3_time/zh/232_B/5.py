def main():
    S = input()
    T = input()
    for i in range(26):
        if S == T:
            print('Yes')
            exit()
        S = S[-1] + S[:-1]
    print('No')
