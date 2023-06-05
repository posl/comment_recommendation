def main():
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    if a <= 8 and b <= 8:
        print("Yay!")
    else:
        print(":(")

if __name__ == '__main__':
    main()