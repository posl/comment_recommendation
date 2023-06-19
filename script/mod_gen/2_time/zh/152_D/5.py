def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            k = str(i)
            l = str(j)
            if k[-1] == l[0] and k[0] == l[-1]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()