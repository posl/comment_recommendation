def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 1
    for i in range(n):
        if s[i] == 'OR':
            ans += 2**(i+1)
    print(ans)

if __name__ == '__main__':
    main()