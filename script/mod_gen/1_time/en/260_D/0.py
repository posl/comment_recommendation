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
        while ans[j] == -1:
            ans[j] = i
            j = p[j]
    for i in range(n):
        print(ans[i] // k + 1)

if __name__ == '__main__':
    main()