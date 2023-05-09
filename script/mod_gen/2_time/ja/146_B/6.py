def main():
    N = int(input())
    S = input()
    ans = ''
    for i in S:
        ans += chr((ord(i)-65+N)%26+65)
    print(ans)

if __name__ == '__main__':
    main()