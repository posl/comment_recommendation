def main():
    A, B, C, X = map(int, input().split())
    print(1-(B-X)/(B-A)*((B-A-C)/(B-A)))

if __name__ == '__main__':
    main()