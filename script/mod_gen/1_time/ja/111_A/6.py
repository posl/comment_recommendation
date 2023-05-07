def main():
    n = str(input())
    n = n.replace('1','9')
    n = n.replace('9','1')
    print(n)

if __name__ == '__main__':
    main()