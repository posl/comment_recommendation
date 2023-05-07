def main():
    rating = int(input())
    if rating < 1200:
        print("ABC")
    elif rating < 2800:
        print("ARC")
    else:
        print("AGC")

if __name__ == '__main__':
    main()