def main():
    v, a, b, c = map(int, input().split())
    if v % a == 0 or v % b == 0 or v % c == 0:
        print("F")
    else:
        if v % a <= v % b and v % a <= v % c:
            print("F")
        elif v % b <= v % a and v % b <= v % c:
            print("M")
        else:
            print("T")

if __name__ == '__main__':
    main()