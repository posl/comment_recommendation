def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S1 = set()
    S2 = set()
    for s in S:
        if s[0] == '!':
            S2.add(s[1:])
        else:
            S1.add(s)
    for s in S1:
        if s in S2:
            print(s)
            return
    print('satisfiable')
