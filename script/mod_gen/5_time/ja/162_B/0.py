def main():
    # input
    N = int(input())
    # compute
    ans = 0
    for i in range(1, N+1):
        if i%3==0 or i%5==0:
            continue
        else:
            ans += i
    # output
    print(ans)

if __name__ == '__main__':
    main()