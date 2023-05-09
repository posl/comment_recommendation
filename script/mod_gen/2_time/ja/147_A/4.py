def main():
    A = [int(x) for x in input().split()]
    if sum(A) >= 22:
        print("bust")
    else:
        print("win")

if __name__ == '__main__':
    main()