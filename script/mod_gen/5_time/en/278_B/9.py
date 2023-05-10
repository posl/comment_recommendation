def main():
    #input
    h, m = map(int, input().split())
    #compute
    if m < 30:
        m += 30
        if h == 0:
            h = 23
        else:
            h -= 1
    else:
        m -= 30
    #output
    print(h, m)

if __name__ == '__main__':
    main()