def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]
    # compute
    ans = 0
    for i in range(N):
        if i+1 == As[As[i]-1]:
            ans += 1
    # output
    print(ans//2)

if __name__ == '__main__':
    main()