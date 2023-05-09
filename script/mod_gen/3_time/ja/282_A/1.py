def main():
    K = int(input())
    ans = ""
    for i in range(K):
        ans += chr(65+i)
    print(ans)

if __name__ == '__main__':
    main()