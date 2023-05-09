def main():
    k = int(input())
    ans = ""
    for i in range(k):
        ans += chr(i+ord("A"))
    print(ans)

if __name__ == '__main__':
    main()