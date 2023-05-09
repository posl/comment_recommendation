def main():
    V, A, B, C = map(int, input().split())
    if V - A <= 0:
        print("F")
    elif V - A - B <= 0:
        print("M")
    elif V - A - B - C <= 0:
        print("T")
    else:
        print("F")

if __name__ == '__main__':
    main()