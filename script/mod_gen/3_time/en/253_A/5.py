def main():
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if (a < b < c) or (c < b < a):
        print("Yes")
    elif (b < a < c) or (c < a < b):
        print("Yes")
    elif (a < c < b) or (b < c < a):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()