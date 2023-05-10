def main():
    n = int(input())
    x = 0
    for i in range(0, 1000001):
        if i**3 > n:
            x = i
            break
    for i in range(0, 1000001):
        if i**3 + i**2 * x + i * x**2 + x**3 >= n:
            print(i**3 + i**2 * x + i * x**2 + x**3)
            break

if __name__ == '__main__':
    main()