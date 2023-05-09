def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = []
    ans.append(max(p[:k]))
    for i in range(k, n):
        if p[i] > ans[-1]:
            ans.append(p[i])
        else:
            ans.append(ans[-1])
    for i in range(len(ans)):
        print(ans[i])
