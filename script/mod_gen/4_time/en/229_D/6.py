def main():
    s = input()
    k = int(input())
    n = len(s)
    s = s.replace('.', '0')
    s = s.replace('X', '1')
    s = list(s)
    s = [int(i) for i in s]
    cumsum = [0]
    for i in range(n):
        cumsum.append(cumsum[i] + s[i])
    ans = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if j - i <= ans:
                continue
            if cumsum[j] - cumsum[i] + k >= j - i:
                ans = max(ans, j - i)
    print(ans)

if __name__ == '__main__':
    main()