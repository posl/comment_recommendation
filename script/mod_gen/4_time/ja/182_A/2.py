def main():
    # input
    A, B = map(int, input().split())
    # compute
    # output
    if B <= 2*A+100:
        print(2*A+100-B)
    else:
        print(0)

if __name__ == '__main__':
    main()