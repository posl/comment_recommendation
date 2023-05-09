def main():
    P = int(input())
    count = 0
    for i in range(10, 0, -1):
        count += P // math.factorial(i)
        P %= math.factorial(i)
    print(count)

if __name__ == '__main__':
    main()