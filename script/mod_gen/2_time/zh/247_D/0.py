def main():
    n = int(input())
    print("1", end="")
    for i in range(n-1):
        print(" " + str(i+2) + " 1", end="")
    print()

if __name__ == '__main__':
    main()