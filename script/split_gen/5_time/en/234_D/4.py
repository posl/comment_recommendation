def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = []
    for i in range(k, n+1):
        ans.append(sorted(p[:i])[k-1])
    for a in ans:
        print(a)
