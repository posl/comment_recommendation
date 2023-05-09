def main():
    a,b,k = map(int,input().split())
    dividers = []
    for i in range(1,min(a,b)+1):
        if a%i == 0 and b%i == 0:
            dividers.append(i)
    print(dividers[-k])

if __name__ == '__main__':
    main()