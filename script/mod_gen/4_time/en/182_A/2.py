def main():
    # Take input Here and Call solution function
    A, B = [int(x) for x in input().split(" ")]
    if B >= 2*A+100:
        print(0)
    else:
        print(2*A+100-B)

if __name__ == '__main__':
    main()