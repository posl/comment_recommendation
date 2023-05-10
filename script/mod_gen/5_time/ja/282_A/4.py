def main():
    k = int(input())
    ans = ''
    for i in range(k):
        ans += chr(65+i)
    print(ans)

if __name__ == '__main__':
    main()