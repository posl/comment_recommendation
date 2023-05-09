def main():
    S = input()
    ans = 0
    for i in range(8):
        ans += S.count(chr(99+i))
    print(ans)

if __name__ == '__main__':
    main()