def main():
    A, B = map(int, input().split())
    if A >= 13 or B >= 13:
        print(":(")
    elif A >= 4 and B >= 4:
        print(":(")
    else:
        print("Yay!")

if __name__ == '__main__':
    main()