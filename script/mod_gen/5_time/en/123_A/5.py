def main():
    # get input
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    # check if antenna pair is greater than k
    if (b - a) > k:
        print(":(")
        return
    elif (c - a) > k:
        print(":(")
        return
    elif (d - a) > k:
        print(":(")
        return
    elif (e - a) > k:
        print(":(")
        return
    elif (c - b) > k:
        print(":(")
        return
    elif (d - b) > k:
        print(":(")
        return
    elif (e - b) > k:
        print(":(")
        return
    elif (d - c) > k:
        print(":(")
        return
    elif (e - c) > k:
        print(":(")
        return
    elif (e - d) > k:
        print(":(")
        return
    else:
        print("Yay!")
        return
main()

if __name__ == '__main__':
    main()