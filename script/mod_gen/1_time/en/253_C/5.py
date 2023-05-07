def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    Q = int(input())
    S = defaultdict(int)
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            S[int(query[1])] += 1
        elif query[0] == '2':
            S[int(query[1])] -= int(query[2])
            if S[int(query[1])] <= 0:
                del S[int(query[1])]
        else:
            print(max(S.keys()) - min(S.keys()))

if __name__ == '__main__':
    main()