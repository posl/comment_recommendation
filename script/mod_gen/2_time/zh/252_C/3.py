def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    ans = 0
    for i in range(10):
        for j in range(n):
            if s[j][i] == str((i+1)%10):
                ans += 1
                break
    print(ans)

if __name__ == '__main__':
    main()