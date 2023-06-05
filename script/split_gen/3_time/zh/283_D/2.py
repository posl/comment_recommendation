def main():
    S = input()
    s = S
    while True:
        if s == '':
            print('是')
            break
        elif s == S:
            print('否')
            break
        else:
            S = s
        s = ''
        for i in range(len(S)):
            if S[i] != '(' and S[i] != ')':
                s += S[i]
            elif S[i] == '(':
                s += S[i]
            elif S[i] == ')':
                if s[-1] == '(':
                    s = s[:-1]
                else:
                    s += S[i]
