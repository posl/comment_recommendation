def main():
    N = int(input())
    S = [input() for i in range(N)]
    S2 = set(S)
    for s in S:
        if s[0] == '!':
            s = s[1:]
            if s in S2:
                pri
