def main():
    V,A,B,C = map(int,input().split())
    if V < A:
        print("F")
    elif V < B:
        print("M")
    elif V < C:
        print("T")
    else:
        print("F")

if __name__ == '__main__':
    main()