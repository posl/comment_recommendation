def main():
    N = input()
    max = 0
    for i in range(1,len(N)):
        a = int(N[0:i])
        b = int(N[i:len(N)])
        if max < a*b:
            max = a*b
    print(max)

if __name__ == '__main__':
    main()