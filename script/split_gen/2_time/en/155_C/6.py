def main():
    from collections import Counter
    N = int(input())
    S = [input() for _ in range(N)]
    C = Counter(S)
    max_count = max(C.values())
    for s in sorted(C.keys()):
        if C[s] == max_count:
            print(s)
main()
