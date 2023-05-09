def main():
    import sys
    from collections import Counter
    N = int(sys.stdin.readline())
    S = [sys.stdin.readline().rstrip() for _ in range(N)]
    C = Counter(S)
    for s in S:
        if C[s] == 1:
            print(s)
        else:
            print(s + '(' + str(C[s] - 1) + ')')
            C[s] -= 1
