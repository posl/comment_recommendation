def main():
    # input
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    # compute
    if e - a <= k:
        ans = 'Yay!'
    else:
        ans = ':('
    # output
    print(ans)

if __name__ == '__main__':
    main()