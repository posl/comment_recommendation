def main():
    n = int(input())
    print(n%10*100 + n//10%10*10 + n//100)

if __name__ == '__main__':
    main()