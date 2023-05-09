def main():
    n = int(input())
    s = input()
    s = s + "0"
    ans = 1
    for i in range(n):
        if s[i] != s[i+1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()