def main():
    #a, b, c = map(int, input().split())
    #print(21 - (a + b + c))
    print(21 - sum(map(int, input().split())))

if __name__ == '__main__':
    main()