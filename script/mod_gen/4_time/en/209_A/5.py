def main():
    # input
    a,b = map(int, input().split())
    # compute
    cnt = 0
    for i in range(a, b+1):
        cnt += 1
    # output
    print(cnt)

if __name__ == '__main__':
    main()