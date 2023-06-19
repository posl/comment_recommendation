def main():
    X = int(input())
    for A in range(-120,120):
        for B in range(-120,120):
            if A**5 - B**5 == X:
                print(A,B)
                return

if __name__ == '__main__':
    main()