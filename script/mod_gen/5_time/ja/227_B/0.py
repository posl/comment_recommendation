def main():
    n = int(input())
    s = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if (s[i] == s[j]):
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()