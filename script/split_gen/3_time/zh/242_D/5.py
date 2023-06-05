def main():
    s = input()
    q = int(input())
    queries = []
    for i in range(q):
        t, k = map(int, input().split())
        queries.append((t, k))
    ans = []
    for t, k in queries:
        for i in range(t):
            s = s.replace("a", "bc").replace("b", "ca").replace("c", "ab")
        ans.append(s[k - 1])
    print(*ans, sep="\n")
