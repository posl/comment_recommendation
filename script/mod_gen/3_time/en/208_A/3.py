def main():
    a, b = map(int, input().split())
    if (a*1 <= b) and (a*6 >= b):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()