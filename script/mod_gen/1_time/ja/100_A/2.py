def main():
    A, B = map(int, input().split())
    if A + B == 16:
        print("Yay!")
    elif A >= 9 or B >= 9:
        print("Yay!")
    else:
        print(":(")

if __name__ == '__main__':
    main()