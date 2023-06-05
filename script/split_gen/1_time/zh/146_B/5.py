def problem146_b():
    N = int(input())
    S = input()
    S = list(S)
    for i in range(len(S)):
        S[i] = chr(ord(S[i]) + N)
        if S[i] > 'Z':
            S[i] = chr(ord(S[i]) - 26)
    print(''.join(S))
