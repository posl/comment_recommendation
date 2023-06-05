def main():
    x = float(input())
    y = int(x*10)%10
    if y < 5:
        print(int(x))
    else:
        print(int(x)+1)

if __name__ == '__main__':
    main()