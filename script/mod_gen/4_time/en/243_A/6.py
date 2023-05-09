def main():
    v, a, b, c = map(int, input().split())
    if v % a == 0:
        if v % b == 0:
            if v % c == 0:
                print("M")
            else:
                print("F")
        else:
            print("T")
    else:
        print("F")

if __name__ == '__main__':
    main()