def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n-2):
        if s[i:i+3] == 'ABC':
            ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()