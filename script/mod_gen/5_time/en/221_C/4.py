def main():
    N = input()
    Max = 0
    for i in range(1, len(N)):
        a = int(N[0:i])
        b = int(N[i:len(N)])
        if Max < a * b:
            Max = a * b
    print(Max)

if __name__ == '__main__':
    main()