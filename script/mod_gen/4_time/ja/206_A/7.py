def main():
    n = int(input())
    n = int(n*1.08)
    if n < 206:
        print("Yay!")
    elif n == 206:
        print("so-so")
    else:
        print(":(")

if __name__ == '__main__':
    main()