def main():
    S = input()
    S = S[::-1]
    for i in range(len(S)):
        if S[i] == '9':
            S = S[:i] + '6' + S[i+1:]
        elif S[i] == '6':
            S = S[:i] + '9' + S[i+1:]
    S = S.replace('0', 'a')
    S = S.replace('1', 'b')
    S = S.replace('9', '0')
    S = S.replace('8', '1')
    S = S.replace('6', '9')
    S = S.replace('a', '0')
    S = S.replace('b', '1')
    print(S)
