def main():
    K = int(input())
    ans = ''
    for i in range(K):
        ans += chr(ord('A') + i)
    print(ans)

if __name__ == '__main__':
    main()