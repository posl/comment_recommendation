def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if str(i)[-1] == str(j)[0]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()