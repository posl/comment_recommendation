def main():
    N = int(input())
    S = [input() for i in range(N)]
    S2 = set(S)
    for s in S:
        if s[0] == '!':
            if s[1:] in S2:
                print(s[1:])
