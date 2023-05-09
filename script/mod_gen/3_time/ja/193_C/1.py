def main():
    N = int(input())
    ans = N - 1
    i = 2
    while i * i <= N:
        j = i * i
        while j <= N:
            ans -= 1
            j *= i
        i += 1
    print(ans)

if __name__ == '__main__':
    main()