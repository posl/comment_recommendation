def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    N = int(input())
    S = defaultdict(lambda: 0)
    for i in range(N):
        s, t = input().split()
        S[s] = int(t)
    S = sorted(S.items(), key=lambda x: x[1], reverse=True)
    print(list(S)[0][0])

if __name__ == '__main__':
    main()