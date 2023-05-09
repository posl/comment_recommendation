def main():
    A = [int(i) for i in input().split()]
    if sum(A) >= 22:
        print("bust")
    else:
        print("win")

if __name__ == '__main__':
    main()