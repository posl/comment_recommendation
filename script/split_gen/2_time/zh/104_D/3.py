def main():
    S = input()
    Q = S.count('?')
    cnt = 0
    for i in range(len(S)):
        if S[i] == 'A':
            cnt += pow(3, Q, 10**9 + 7)
        elif S[i] == 'B':
            cnt += pow(3, Q, 10**9 + 7) * 2
        elif S[i] == 'C':
            cnt += pow(3, Q, 10**9 + 7) * 4
        else:
            cnt += pow(3, Q - 1, 10**9 + 7)
            if i < len(S) - 1:
                if S[i + 1] == 'A':
                    cnt += pow(3, Q - 1, 10**9 + 7)
                elif S[i + 1] == 'B':
                    cnt += pow(3, Q - 1, 10**9 + 7) * 2
                elif S[i + 1] == 'C':
                    cnt += pow(3, Q - 1, 10**9 + 7) * 4
            if i < len(S) - 2:
                if S[i + 2] == 'A':
                    cnt += pow(3, Q - 2, 10**9 + 7)
                elif S[i + 2] == 'B':
                    cnt += pow(3, Q - 2, 10**9 + 7) * 2
                elif S[i + 2] == 'C':
                    cnt += pow(3, Q - 2, 10**9 + 7) * 4
    print(cnt % (10**9 + 7))
