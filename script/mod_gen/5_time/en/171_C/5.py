def main():
    n = int(input())
    ans = ""
    while n:
        ans += chr((n-1)%26+97)
        n = (n-1)//26
    print(ans[::-1])

if __name__ == '__main__':
    main()