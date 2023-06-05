def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    s = [int(i) for i in s]
    s1 = [0] * n
    s2 = [0] * n
    for i in range(n):
        if s[i] == 0:
            s1[i] = w[i]
        else:
            s2[i] = w[i]
    s1.sort()
    s2.sort()
    for i in range(n - 1):
        s1[i + 1] += s1[i]
        s2[i + 1] += s2[i]
    ans = 0
    for i in range(n + 1):
        if i < n:
            ans = max(ans, s1[i])
        if i > 0:
            ans = max(ans, s2[i - 1])
    print(ans)

if __name__ == '__main__':
    main()