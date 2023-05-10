def main():
    from collections import defaultdict
    import sys
    input = sys.stdin.readline
    N = int(input())
    S = defaultdict(int)
    max_s = 0
    min_s = 10**9
    for _ in range(N):
        q = input().split()
        if q[0] == '1':
            S[q[1]] += 1
            max_s = max(max_s, int(q[1]))
            min_s = min(min_s, int(q[1]))
        elif q[0] == '2':
            n = S[q[1]]
            if n <= int(q[2]):
                S[q[1]] = 0
            else:
                S[q[1]] -= int(q[2])
            if S[q[1]] == 0:
                del S[q[1]]
        else:
            print(max_s - min_s)

if __name__ == '__main__':
    main()