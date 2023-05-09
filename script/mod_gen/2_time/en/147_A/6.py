def main():
    A = [int(a) for a in input().split()]
    if sum(A) >= 22:
        print("bust")
    else:
        print("win")

if __name__ == '__main__':
    main()