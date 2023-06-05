def main():
    num = input()
    num = num.replace('1','a').replace('9','1').replace('a','9')
    print(num)

if __name__ == '__main__':
    main()