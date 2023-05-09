def main():
    V, A, B, C = map(int, input().split())
    if V % A == 0 and V % B == 0 and V % C == 0:
        print("F")
    elif V % A == 0 and V % B == 0:
        print("T")
    elif V % A == 0 and V % C == 0:
        print("M")
    elif V % B == 0 and V % C == 0:
        print("F")
    elif V % A == 0:
        print("M")
    elif V % B == 0:
        print("T")
    elif V % C == 0:
        print("F")
    else:
        print("M")

if __name__ == '__main__':
    main()