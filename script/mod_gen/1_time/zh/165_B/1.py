def main():
    x = int(input())
    i = 0
    a = 100
    while a < x:
        a = int(a * 1.01)
        i += 1
    print(i)

if __name__ == '__main__':
    main()