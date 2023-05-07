def main():
    import sys
    sys.setrecursionlimit(100000)
    input = sys.stdin.readline
    S, K = input().split()
    K = int(K)
    S = sorted(S)
    #print(S)
    #print(K)
    def dfs(s, k):
        if s == "":
            return ""
        #print("s", s, "k", k)
        for i, c in enumerate(s):
            #print("i", i, "c", c)
            #print("len(s[:i]+s[i+1:])", len(s[:i]+s[i+1:]))
            #print("fact(len(s[:i]+s[i+1:]))", fact(len(s[:i]+s[i+1:])))
            if fact(len(s[:i]+s[i+1:])) < k:
                k -= fact(len(s[:i]+s[i+1:]))
            else:
                return c + dfs(s[:i]+s[i+1:], k)
    def fact(n):
        if n == 0:
            return 1
        else:
            return n * fact(n-1)
    print(dfs(S, K))

if __name__ == '__main__':
    main()