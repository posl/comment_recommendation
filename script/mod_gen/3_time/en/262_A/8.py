def main():
    # get input
    y = int(input())
    # solve
    ans = y + 2 - (y % 4)
    # output
    print(ans)

if __name__ == '__main__':
    main()