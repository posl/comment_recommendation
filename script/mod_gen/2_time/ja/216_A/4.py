def main():
    x = float(input())
    if x - int(x) < 0.3:
        print(int(x)-1)
    elif x - int(x) < 0.7:
        print(int(x))
    else:
        print(int(x)+1)

if __name__ == '__main__':
    main()