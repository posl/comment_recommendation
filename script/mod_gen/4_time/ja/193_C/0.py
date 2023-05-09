def main():
    N = int(input())
    ans = N
    i = 2
    while i*i <= N:
        j = 2
        while i**j <= N:
            ans -= 1
            j += 1
        i += 1
    print(ans)

if __name__ == '__main__':
    main()