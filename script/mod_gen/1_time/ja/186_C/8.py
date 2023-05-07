def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if not(str(7) in str(i) or str(7) in oct(i)):
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()