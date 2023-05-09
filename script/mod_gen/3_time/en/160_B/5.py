def main():
    X = int(input())
    happiness = 0
    happiness += X//500 * 1000
    happiness += X%500//5 * 5
    print(happiness)

if __name__ == '__main__':
    main()