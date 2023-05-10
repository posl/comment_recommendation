def main():
    X = int(input())
    for A in range(-118,119):
        for B in range(-119,118):
            if A**5 - B**5 == X:
                print(A,B)
                exit()

if __name__ == '__main__':
    main()