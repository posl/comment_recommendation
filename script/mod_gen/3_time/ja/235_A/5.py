def main():
    abc = int(input())
    a = abc//100
    b = (abc%100)//10
    c = (abc%100)%10
    print(a+b+c + b+c+a + c+a+b)

if __name__ == '__main__':
    main()