def main():
    V,A,B,C = map(int,input().split())
    if V <= A:
        print("F")
    elif V <= A+B:
        print("F")
    elif V <= A+B+C:
        print("M")
    else:
        print("T")

if __name__ == '__main__':
    main()