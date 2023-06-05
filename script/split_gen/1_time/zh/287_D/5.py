def main():
    S = input()
    T = input()
    for i in range(len(S) - len(T) + 1):
        if S[i] == T[0] or S[i] == '?':
            for j in range(len(T)):
                if S[i + j] != T[j] and S[i + j] != '?':
                    break
            else:
                print('YES')
                continue
        print('NO')
