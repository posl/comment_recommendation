def check():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for s in S:
        if s[0] == '!':
            if s[1:] in S:
                return s[1:]
