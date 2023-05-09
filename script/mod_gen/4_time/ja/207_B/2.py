def main():
    # input
    A, B, C, D = map(int, input().split())
    # compute
    ans = -1
    for i in range(10**5):
        if A <= C * i - B * i * D:
            ans = i
            break
    # output
    print(ans)

if __name__ == '__main__':
    main()