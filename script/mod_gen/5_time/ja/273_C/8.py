def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    from collections import Counter
    N = int(readline())
    A = list(map(int,readline().split()))
    c = Counter(A)
    c = sorted(c.items(),key=lambda x:x[0])
    ans = [0]*N
    for i in range(N):
        if c[i][0] > i:
            ans[i] = c[i][1]
    print(*ans,sep='\n')

if __name__ == '__main__':
    main()