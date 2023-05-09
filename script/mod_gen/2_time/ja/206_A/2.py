def main():
    N = int(input())
    if N*108//100 < 206:
        print("Yay!")
    elif N*108//100 == 206:
        print("so-so")
    else:
        print(":(")

if __name__ == '__main__':
    main()