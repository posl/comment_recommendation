def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    #print(s)
    #print(len(s))
    cnt = 0
    for i in range(n+1):
        for j in range(i+1, n+1):
            if s[j] - s[i] == k:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()