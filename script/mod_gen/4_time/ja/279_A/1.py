def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == "v":
            ans += (n-i-1)*(i+1)
    print(ans)
main()

if __name__ == '__main__':
    main()