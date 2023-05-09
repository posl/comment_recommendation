def main():
    a, b = input().split()
    if int(a) > int(b):
        print(b * int(a))
    else:
        print(a * int(b))

if __name__ == '__main__':
    main()