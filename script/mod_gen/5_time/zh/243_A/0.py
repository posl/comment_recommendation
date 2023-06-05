def main():
    v,a,b,c = map(int, input().split())
    if v % 3 == 0:
        print("F")
    elif v % 3 == 1:
        print("M")
    elif v % 3 == 2:
        print("T")

if __name__ == '__main__':
    main()