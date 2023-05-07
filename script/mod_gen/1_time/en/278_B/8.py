def main():
    H, M = map(int, input().split())
    #print(H, M)
    if (H == 23 and M == 59):
        print("0 0")
    else:
        if (M == 59):
            print(H + 1, "0")
        else:
            print(H, M + 1)

if __name__ == '__main__':
    main()