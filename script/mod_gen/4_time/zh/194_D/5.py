def main():
    N = int(input())
    #print(N)
    ans = 0
    for i in range(1,N+1):
        ans += (1/i)
    print(ans)
    return

if __name__ == '__main__':
    main()