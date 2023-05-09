def main():
    n = int(input())
    n = str(n)
    n = n.replace('9','a')
    n = n.replace('1','9')
    n = n.replace('a','1')
    print(n)

if __name__ == '__main__':
    main()