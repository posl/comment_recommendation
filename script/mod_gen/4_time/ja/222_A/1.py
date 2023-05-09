def main():
    # input
    N = input()
    # solve
    if len(N) == 4:
        print(N)
    elif len(N) == 3:
        print("0"+N)
    elif len(N) == 2:
        print("00"+N)
    else:
        print("000"+N)

if __name__ == '__main__':
    main()