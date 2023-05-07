def main():
    A, B = map(int, input().split())
    if A + B <= 16 and max(A, B) <= 8:
        print("Yay!")
    else:
        print(":(")

if __name__ == '__main__':
    main()