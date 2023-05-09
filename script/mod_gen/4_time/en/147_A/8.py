def main():
    line = input().split()
    A = [int(i) for i in line]
    if sum(A) >= 22:
        print("bust")
    else:
        print("win")

if __name__ == '__main__':
    main()