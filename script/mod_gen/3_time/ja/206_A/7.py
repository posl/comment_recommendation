def main():
    n = int(input())
    m = int(n * 1.08)
    if m < 206:
        print("Yay!")
    elif m == 206:
        print("so-so")
    else:
        print(":(")

if __name__ == '__main__':
    main()