def main():
    k = int(input())
    a = ord('A')
    for i in range(k):
        print(chr(a+i), end="")
    print()

if __name__ == '__main__':
    main()