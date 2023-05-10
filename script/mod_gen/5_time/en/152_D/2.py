def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if int(str(i)[0]) == int(str(i)[-1]):
            ans += 1
    print(ans)
    return 0

if __name__ == '__main__':
    main()