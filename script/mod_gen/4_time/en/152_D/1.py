def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        i = str(i)
        if i[0] == i[-1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()