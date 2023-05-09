def main():
    k = int(input())
    ans = ""
    for i in range(k):
        ans += chr(ord('A') + i)
    print(ans)

if __name__ == '__main__':
    main()