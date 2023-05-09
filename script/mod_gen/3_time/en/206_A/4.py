def main():
    n = int(input())
    x = int(n * 1.08)
    if x < 206:
        print("Yay!")
    elif x == 206:
        print("so-so")
    else:
        print(":(")

if __name__ == '__main__':
    main()