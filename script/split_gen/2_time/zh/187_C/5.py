def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S = set(S)
    for s in S:
        if s[0] == '!':
            s = s[1:]
            if s in S:
                print(s)
