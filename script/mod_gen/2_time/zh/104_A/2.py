def main():
    # input
    R = int(input())
    # compute
    if R < 1200:
        ans = "ABC"
    elif R < 2800:
        ans = "ARC"
    else:
        ans = "AGC"
    # output
    print(ans)

if __name__ == '__main__':
    main()