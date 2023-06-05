def main():
    x = int(input())
    #print(x)
    #print(type(x))
    #print(x//500)
    #print(x%500)
    #print((x%500)//5)
    #print((x%500)%5)
    print((x//500)*1000 + ((x%500)//5)*5)

if __name__ == '__main__':
    main()