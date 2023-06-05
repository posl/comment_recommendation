def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if int(str(i)[-1]) == int(str(j)[0]) and int(str(i)[0]) == int(str(j)[-1]):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()