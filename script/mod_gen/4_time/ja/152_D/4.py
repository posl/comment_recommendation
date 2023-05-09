def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if i%10 == int(str(i)[0]) and int(str(i)[-1]) == int(str(i)[0]):
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()