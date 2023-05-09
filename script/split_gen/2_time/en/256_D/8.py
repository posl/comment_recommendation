def main():
    N = int(input())
    A = []
    for _ in range(N):
        s, t = map(int, input().split())
        A.append((s, t))
    A.sort()
    ans = []
    l, r = A[0]
    for s, t in A[1:]:
        if r < s:
            ans.append((l, r))
            l, r = s, t
        else:
            r = max(r, t)
    ans.append((l, r))
    for l, r in ans:
        print(l, r)
