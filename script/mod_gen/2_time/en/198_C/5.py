def main():
    R, X, Y = map(int, input().split())
    distance = (X**2 + Y**2)**(1/2)
    if distance == R:
        print(1)
    elif distance < R:
        print(2)
    else:
        print(int(distance//R) + (1 if distance % R else 0))
main()

if __name__ == '__main__':
    main()