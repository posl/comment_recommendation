def main():
    x = float(input())
    if 0 <= x <= 2:
        print("X-")
    elif 3 <= x <= 6:
        print("X")
    else:
        print("X+")

if __name__ == '__main__':
    main()