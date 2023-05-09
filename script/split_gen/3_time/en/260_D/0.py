def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = [0] * n
    for i in range(n):
        c[p[i] - 1] = i
    s = [0] * n
    for i in range(n):
        s[i] = i // k
    ans = [-1] * n
    for i in range(n):
        if ans[i] != -1:
            continue
        j = i
        while ans[j] == -1:
            ans[j] = i + 1
            j = c[j]
            if s[j] == s[i]:
                break
            j = (j // k) * k
    for i in range(n):
        print(ans[i])
main()
