def main():
    abc = int(input())
    #print(abc)
    a = abc // 100
    b = (abc - a * 100) // 10
    c = abc % 10
    #print(a,b,c)
    print(a+b+c + b+c+a + c+a+b)

if __name__ == '__main__':
    main()