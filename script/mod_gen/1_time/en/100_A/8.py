def main():
    # Read input
    A,B = map(int,input().split())
    # Logic
    if A <= 8 and B <= 8:
        # Output
        print("Yay!")
    else:
        print(":(")

if __name__ == '__main__':
    main()