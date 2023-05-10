def main():
    N = int(input())
    if int(N * 1.08) < 206:
        print("Yay!")
    elif int(N * 1.08) == 206:
        print("so-so")
    else:
        print(":(")

if __name__ == '__main__':
    main()