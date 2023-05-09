def main():
    k = int(input())
    ans = ""
    for i in range(k):
        ans += chr(i+65)
    print(ans)

if __name__ == '__main__':
    main()