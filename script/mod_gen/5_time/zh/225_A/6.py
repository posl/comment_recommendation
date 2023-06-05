def main():
    s = input()
    n = len(s)
    a = 1
    for i in range(1, n+1):
        a *= i
    print(a)

if __name__ == '__main__':
    main()