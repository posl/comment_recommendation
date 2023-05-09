def main():
    from sys import stdin
    from bisect import bisect_left
    from collections import deque
    def input():
        return stdin.readline().strip()
    N, K = map(int, input().split())
    P = [int(p) for p in input().split()]
    # 1-indexed
    d = deque()
    ans = [-1] * N
    for i, p in enumerate(P):
        # print(d)
        # print(ans)
        if d and d[-1] < p:
            while d and d[-1] < p:
                ans[d.pop()-1] = i+1
        d.append(p)
        if len(d) == K:
            while d:
                ans[d.pop()-1] = i+1
    print('
'.join(map(str, ans)))

if __name__ == '__main__':
    main()