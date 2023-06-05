def main():
    n = int(input())
    ans = int(n * 1.08)
    if ans < 206:
        print("Yay!")
    elif ans == 206:
        print("so-so")
    else:
        print(":(")

if __name__ == '__main__':
    main()