def main():
    A = input().split()
    A = [int(a) for a in A]
    if sum(A) >= 22:
        print("bust")
    else:
        print("win")

if __name__ == '__main__':
    main()