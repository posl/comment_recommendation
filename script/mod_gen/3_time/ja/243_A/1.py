def main():
    V, A, B, C = map(int, input().split())
    if V % A == 0:
        print("F")
    elif V % B == 0:
        print("M")
    elif V % C == 0:
        print("T")
    else:
        print("F")

if __name__ == '__main__':
    main()