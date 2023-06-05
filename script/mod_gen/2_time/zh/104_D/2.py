def main():
    S = input()
    Q = S.count('?')
    A = 0
    B = 0
    C = 0
    for i in range(len(S)):
        if S[i] == 'A':
            A += 1
        elif S[i] == 'B':
            B += 1
        elif S[i] == 'C':
            C += 1
    print((A*B*C)%1000000007)

if __name__ == '__main__':
    main()