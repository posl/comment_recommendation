def main():
    N = int(input())
    S = input()
    ans = ""
    for s in S:
        ans += chr((ord(s) - ord("A") + N) % 26 + ord("A"))
    print(ans)

if __name__ == '__main__':
    main()