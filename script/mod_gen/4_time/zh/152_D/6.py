def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        str_i = str(i)
        if str_i[0] == str_i[-1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()