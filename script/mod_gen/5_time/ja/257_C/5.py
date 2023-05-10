def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    w1 = [0] * n
    w2 = [0] * n
    for i in range(n):
        if s[i] == '0':
            w1[i] = w[i]
        else:
            w2[i] = w[i]
    for i in range(1, n):
        w1[i] += w1[i-1]
        w2[i] += w2[i-1]
    ans = 0
    for i in range(n):
        if s[i] == '0':
            ans = max(ans, w1[i] + w2[n-1] - w2[i])
        else:
            ans = max(ans, w2[i] + w1[n-1] - w1[i])
    print(ans)

if __name__ == '__main__':
    main()