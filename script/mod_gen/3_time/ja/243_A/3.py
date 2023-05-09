def main():
    V, A, B, C = map(int, input().split())
    if V <= A:
        print("T")
    elif V <= A + B:
        print("M")
    else:
        print("F")

if __name__ == '__main__':
    main()