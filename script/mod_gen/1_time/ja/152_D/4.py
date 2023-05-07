def main():
    N = int(input())
    if N < 10:
        print(N)
        return
    else:
        ans = 9
        for i in range(10,N+1):
            if str(i)[0] == str(i)[len(str(i))-1]:
                ans += 1
        print(ans)
main()

if __name__ == '__main__':
    main()