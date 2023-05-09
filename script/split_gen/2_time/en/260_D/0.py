def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = [-1] * n
    for i in range(n):
        p[i] -= 1
    for i in range(n):
        if ans[i] != -1:
            continue
        j = i
        while True:
            ans[j] = i + 1
            j = p[j]
            if ans[j] != -1:
                break
    for i in range(n):
        print(ans[i])
