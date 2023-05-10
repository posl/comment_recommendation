def main():
    a, b = map(int, input().split())
    #print(a, b)
    #print(a / (a + b), b / (a + b))
    print("{:.12f} {:.12f}".format(a / (a + b), b / (a + b)))

if __name__ == '__main__':
    main()