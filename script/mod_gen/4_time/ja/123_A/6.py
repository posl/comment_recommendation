def main():
    # input
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    # check
    if b - a > k:
        print(":(")
    elif c - a > k:
        print(":(")
    elif d - a > k:
        print(":(")
    elif e - a > k:
        print(":(")
    elif c - b > k:
        print(":(")
    elif d - b > k:
        print(":(")
    elif e - b > k:
        print(":(")
    elif d - c > k:
        print(":(")
    elif e - c > k:
        print(":(")
    elif e - d > k:
        print(":(")
    else:
        print("Yay!")

if __name__ == '__main__':
    main()