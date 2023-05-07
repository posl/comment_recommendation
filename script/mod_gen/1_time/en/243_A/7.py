def main():
    V, A, B, C = map(int, input().split())
    if A > B:
        if B > C:
            print("T")
        else:
            if A > C:
                print("T")
            else:
                print("F")
    else:
        if A > C:
            print("T")
        else:
            if B > C:
                print("T")
            else:
                print("M")

if __name__ == '__main__':
    main()